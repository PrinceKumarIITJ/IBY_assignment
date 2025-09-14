from transformers import pipeline

# Load summarizer once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_notes(section: str, max_length: int = 150) -> str:
    """Summarize a section into concise notes."""
    result = summarizer(section, max_length=max_length, min_length=50, do_sample=False)
    return result[0]['summary_text']

def generate_quiz(section: str) -> list:
    """
    Dummy quiz generator.
    (Later: fine-tune T5/BART on QA datasets for real MCQs.)
    """
    sentences = section.split(". ")
    quiz = []
    for i, s in enumerate(sentences[:3]):  # first 3 sentences
        quiz.append(f"Q{i+1}: What is meant by '{s[:40]}...' ?")
    return quiz
