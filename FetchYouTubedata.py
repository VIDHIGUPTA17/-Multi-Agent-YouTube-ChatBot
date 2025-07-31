# from youtube_transcript_api import YouTubeTranscriptApi
# import os
# from groq import Groq  # Install with: pip install groq

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# def get_transcript(video_url):
#     video_id = video_url.split("v=")[-1]
#     transcript = YouTubeTranscriptApi.get_transcript(video_id)
#     full_text = " ".join([entry['text'] for entry in transcript])
#     return full_text



# def summarize_text(text):
#     prompt = f"Summarize this video transcript:\n\n{text[:3000]}"  # LLM token limit
#     chat_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": prompt}],
#         model="llama3-8b-8192",
#     )
#     return chat_completion.choices[0].message.content



import os
from youtube_transcript_api import YouTubeTranscriptApi
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_transcript(video_url):
    video_id = video_url.split("v=")[-1].split("&")[0]  # Extract only the video ID
    
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)
    
    full_text = " ".join([entry.text for entry in transcript])
    return full_text

def summarize_text(text):
    prompt = f"Summarize this video transcript:\n\n{text[:3000]}"
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
