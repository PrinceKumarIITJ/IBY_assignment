from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url: str) -> str:
    """Extract video ID from YouTube URL."""
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return url

def get_youtube_transcript(url: str) -> str:
    """Fetch YouTube transcript as plain text."""
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    return " ".join([t['text'] for t in transcript])
