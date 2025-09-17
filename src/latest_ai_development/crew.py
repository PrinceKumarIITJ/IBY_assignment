from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    SerperDevTool, 
    ScrapeWebsiteTool,
    WebsiteSearchTool,
    ArxivPaperTool
)
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.tools import Tool
from crewai.tools import BaseTool

from langchain.vectorstores import Chroma


from typing import Type, Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class PDFSearchToolInput(BaseModel):
    """Input schema for PDFSearchTool."""
    query: str = Field(..., description="Search query to find relevant content in the PDF")

class PDFSearchTool(BaseTool):
    name: str = "PDF Search Tool"
    description: str = "Search through PDF contents using semantic similarity"
    args_schema: Type[BaseModel] = PDFSearchToolInput
    
    def __init__(self, vectorstore: Any, pdf_name: str, **kwargs):
        # Set dynamic name and description
        super().__init__(
            name=f"PDF Search: {pdf_name}",
            description=f"Search through the contents of {pdf_name} using semantic similarity.",
            **kwargs
        )
        self._vectorstore = vectorstore

    def _run(self, query: str) -> str:
        """Execute the search query against the PDF vectorstore"""
        results = self._vectorstore.similarity_search(query, k=3)
        return "\n\n".join([doc.page_content for doc in results])


class RoutingDecision(BaseModel):
    tools: List[str] = Field(description="List of selected tools for research")
    priority: str = Field(description="Research priority level")
    reasoning: str = Field(description="Explanation of tool selection")
    research_strategy: str = Field(description="Overall research approach")

@CrewBase
class LatestAiDevelopment():
    """Enhanced LatestAiDevelopment crew with proper tool assignment"""

    def __init__(self, llm_model=None, llm_config=None, file_paths=None,*args, **kwargs):
        super().__init__()
        self.llm_model = llm_model
        self.llm_config = llm_config or {}
        self.file_paths = file_paths or []
        
        # Initialize tools
        self._setup_tools()
    
    def _setup_tools(self):
        """Setup tools: web + optional semantic PDF search"""
        self.serper_tool = SerperDevTool(n_results=1)
        self.web_search_tool = WebsiteSearchTool()
        self.scrape_tool = ScrapeWebsiteTool()
        self.arxiv_tool = ArxivPaperTool(download_pdfs=False, save_dir="./arxiv_pdfs")

        self.pdf_tools = []
        if self.file_paths:
            for file_path in self.file_paths:
                if file_path.endswith('.pdf') and os.path.exists(file_path):
                    loader = PyPDFLoader(file_path)
                    documents = loader.load()

                    text_splitter = RecursiveCharacterTextSplitter(
                        chunk_size=1000,
                        chunk_overlap=100
                    )
                    docs = text_splitter.split_documents(documents)

                    embeddings = HuggingFaceEmbeddings(
                        model_name="BAAI/bge-small-en-v1.5"
                    )

                    persist_directory = "./chroma_db"
                    os.makedirs(persist_directory, exist_ok=True)

                    vectorstore = Chroma.from_documents(
                        docs,
                        embeddings,
                        collection_name=os.path.basename(file_path).replace(".pdf", "_collection"),
                        persist_directory=persist_directory
                    )

                    # Use the corrected PDFSearchTool
                    pdf_tool = PDFSearchTool(
                        vectorstore=vectorstore, 
                        pdf_name=os.path.basename(file_path)
                    )
                    self.pdf_tools.append(pdf_tool)

    @agent
    def router_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['router_agent'],
            verbose=True,
            llm=self.llm_model,
            max_iter=2,
            max_execution_time=100
        )
    
    @agent  
    def rag_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['rag_specialist'],
            verbose=True,
            llm=self.llm_model,
            tools=self.pdf_tools,   # only semantic PDF search tools now
            max_iter=1,
            max_execution_time=100
        )
    
    @agent
    def web_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['web_researcher'],
            verbose=True,
            llm=self.llm_model,
            tools=[
                self.serper_tool,
                self.web_search_tool,
                self.scrape_tool,
                self.arxiv_tool
            ],
            max_iter=1,
            max_execution_time=100,
            memory=False
        )
    
    @agent
    def synthesis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['synthesis_agent'],
            verbose=True,
            llm=self.llm_model,
            max_iter=1,
            max_execution_time=180
        )
    
    # ---------------- Tasks ----------------
    @task
    def routing_task(self) -> Task:
        return Task(
            config=self.tasks_config['routing_task'],
            agent=self.router_agent(),
            output_pydantic=RoutingDecision
        )
    
    @task
    def rag_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['rag_research_task'],
            agent=self.rag_specialist(),
            context=[self.routing_task()]
        )
    
    @task
    def web_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_research_task'],
            agent=self.web_researcher(),
            context=[self.routing_task()]
        )
    
    @task
    def synthesis_task(self) -> Task:
        return Task(
            config=self.tasks_config['synthesis_task'],
            agent=self.synthesis_agent(),
            context=[self.rag_research_task(), self.web_research_task()],
            output_file='final_research_report.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the enhanced LatestAiDevelopment crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            max_rpm=30,
        )
