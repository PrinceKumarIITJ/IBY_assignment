# AI Agent for Automated Social Media Content Generation

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-LangChain-green?style=for-the-badge" alt="Framework">
  <img src="https://img.shields.io/badge/Model-Llama_3-purple?style=for-the-badge" alt="Model">
  <img src="https://img.shields.io/badge/Fine--Tuning-LoRA-orange?style=for-the-badge" alt="Fine-Tuning">
</div>

---

### Applicant Details
* **Name**: Prince Kumar
* **University**: Indian Institute of Technology Jodhpur (IIT Jodhpur)
* **Department**: Computer Science and Engineering

---

## 📖 About The Project

This project is an AI agent designed to automate the manual task of creating social media content. Developed as part of the Data Science Internship assignment for **I'm beside you**, this agent can take a single theme from a user and generate a complete, structured social media post, such as an Instagram carousel.

The agent demonstrates a sophisticated architecture involving reasoning, planning, and execution. It utilizes a **multi-agent system** and integrates a **custom fine-tuned Large Language Model (LLM)** to ensure high-quality, reliable, and stylistically consistent outputs.

## ✨ Key Features

* [cite_start]**🤖 Multi-Agent Architecture**: Implements a Planner agent for creating a content strategy and an Executor agent for generating the content[cite: 14].
* [cite_start]**🎯 Specialized Fine-Tuned Model**: Uses a Llama-3 8B model fine-tuned with **LoRA (Low-Rank Adaptation)** to generate perfectly structured JSON output for carousels[cite: 5, 7].
* **⚡ High-Speed Generation**: Leverages the **Groq API** for near-instantaneous planning and generation steps.
* [cite_start]**📈 Built-in Evaluation**: Includes an evaluation module that uses an "LLM-as-a-judge" methodology to score the generated content on quality and reliability.
* **🔧 Extensible and Modular**: The code is structured into clear components for models, agents, and evaluation, making it easy to extend.

## 🏗️ Architecture Overview

The agent's workflow is designed to mimic a human content creator's thought process:

1.  **Input Theme**: The user provides a simple theme (e.g., "The Power of Compounding").
2.  [cite_start]**Planner Agent**: This agent, powered by `llama3` via the Groq API, receives the theme and creates a structured, step-by-step plan for the content[cite: 14].
3.  [cite_start]**Executor Agent**: This agent takes the plan and uses the custom **fine-tuned LoRA model** to generate the content for each step, ensuring it adheres to the required JSON format[cite: 14].
4.  **Final Output**: The agent assembles the pieces into a complete social media post, ready for the user.

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

* Python 3.10+
* An API key from [Groq](https://console.groq.com/keys)
* A local installation of [Ollama](https://ollama.com/) with the `llama3` model pulled.
    ```sh
    ollama pull llama3
    ```

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/PrinceKumarIITJ/IBY_assignment.git](https://github.com/PrinceKumarIITJ/IBY_assignment.git)
    cd IBY_assignment
    ```

2.  **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a file named `.env` in the root directory and add your Groq API key:
    ```
    GROQ_API_KEY="your_api_key_here"
    ```

## 💻 Usage

To run the agent, execute the `main.py` script. It will run a predefined example to generate an Instagram carousel post on the theme "The Power of Compounding".

```sh
python main.py