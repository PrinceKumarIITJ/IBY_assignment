from utils import get_youtube_transcript
from planner import plan_sections
from executor import generate_notes, generate_quiz

def run_agent(youtube_url: str):
    # Step 1: Get transcript
    transcript = get_youtube_transcript(youtube_url)
    print("✅ Transcript fetched!")

    # Step 2: Planner splits transcript
    sections = plan_sections(transcript)
    print(f"📑 Transcript split into {len(sections)} sections.")

    all_notes, all_quiz = [], []

    # Step 3: Executor processes each section
    for i, sec in enumerate(sections[:3]):  # limit for demo
        notes = generate_notes(sec)
        quiz = generate_quiz(sec)

        all_notes.append(f"--- Section {i+1} ---\n{notes}")
        all_quiz.extend(quiz)

    return "\n".join(all_notes), "\n".join(all_quiz)

if __name__ == "__main__":
    url = input("🎥 Enter YouTube lecture URL: ")
    notes, quiz = run_agent(url)

    print("\n📝 Generated Notes:\n", notes)
    print("\n❓ Practice Quiz:\n", quiz)
