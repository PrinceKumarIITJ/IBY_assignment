import streamlit as st
from latest_ai_development.crew import LatestAiDevelopment
from datetime import datetime
import os
import traceback

st.title("Multi-Agent Researcher")

# LLM Selection
llm_options = {
    "OpenAI GPT-4": "openai/gpt-4",
    "OpenAI GPT-3.5": "openai/gpt-3.5-turbo", 
    "Gemini 2.0 flash": "gemini/gemini-2.0-flash-001",
    "Gemini 2.5 flash preview": "gemini/gemini-2.5-flash-preview-04-17",
    "Gemini 1.5 flash": "gemini/gemini-1.5-flash",
    "Ollama | Qwen2.5": "ollama/qwen2.5:0.5b"
}

selected_llm = st.selectbox("Choose LLM Model:", list(llm_options.keys()), index=0)

question = st.text_area(
    "Enter your research question:", 
    "What are the latest advancements in AI LLMs?", 
    height=100
)

research_depth = st.selectbox(
    "Research Depth:",
    ["Quick Overview", "Detailed Analysis", "Comprehensive Research"],
    index=1
)

# File upload
uploaded_files = st.file_uploader(
    "Upload documents (PDF, TXT, MD)", 
    type=["pdf", "txt", "md"],
    accept_multiple_files=True
)

if st.button("Run Enhanced Crew", type="primary"):
    llm_model = llm_options[selected_llm]
    
    try:
        # Handle file uploads
        file_paths = []
        if uploaded_files:
            os.makedirs("./uploaded_docs", exist_ok=True)
            for uploaded_file in uploaded_files:
                file_path = f"./uploaded_docs/{uploaded_file.name}"
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                file_paths.append(file_path)
                st.success(f"Uploaded: {uploaded_file.name}")
        
        # Progress section - full width
        st.header("🤖 Crew Progress")
        progress_bar = st.progress(0)
        status_placeholder = st.empty()
        
        inputs = {
            'current_year': str(datetime.now().year),
            'question': question,
            'research_depth': research_depth
        }
        
        progress_bar.progress(25)
        status_placeholder.text("🔄 Initializing crew...")
        
        crew_instance = LatestAiDevelopment(
            llm_model=llm_model, 
            file_paths=file_paths,
            knowledge_dir=None
        ).crew()
        
        progress_bar.progress(50)
        status_placeholder.text("🔄 Running research...")
        
        result = crew_instance.kickoff(inputs=inputs)
        
        progress_bar.progress(100)
        status_placeholder.text("✅ Research completed!")
        
        # Results section - full width
        st.header("📊 Research Results")
        st.markdown(str(result))
                    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        with st.expander("Error Details"):
            st.code(traceback.format_exc())
