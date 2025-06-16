# summarizer.py

from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re

def extract_video_id(url):
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if not video_id_match:
        raise ValueError("Invalid YouTube URL")
    return video_id_match.group(1)

def get_transcript(video_id):
    transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = " ".join([item["text"] for item in transcript_data])
    return transcript_text

def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, summarizer):
    max_chunk = 1000
    text_chunks = [text[i:i + max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ""
    for chunk in text_chunks:
        summary_piece = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        summary += summary_piece.strip() + " "
    return summary.strip()
