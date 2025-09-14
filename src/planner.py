def plan_sections(transcript: str, chunk_size: int = 500) -> list:
    """
    Splits transcript into sections for processing.
    Each section ~500 words.
    """
    words = transcript.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]
