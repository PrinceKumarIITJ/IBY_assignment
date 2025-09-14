from utils import get_youtube_transcript
from executor import generate_notes

def main():
    print("🎓 YouTube Lecture Agent – Demo")
    url = input("Enter YouTube video URL: ")
    
    # Step 1: Get transcript
    transcript = get_youtube_transcript(url)
    print("\n📜 Transcript fetched successfully!\n")
    
    # Step 2: Generate notes
    notes = generate_notes(transcript)
    print("📝 Generated Notes:\n")
    print(notes)

if __name__ == "__main__":
    main()
