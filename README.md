🎥 Multi-Agent YouTube ChatBot (Groq + LLaMA3)
This is a multi-agent conversational AI application powered by [LLaMA3 via Groq API] and [LangChain], designed to extract, summarize, and chat interactively about YouTube videos. It uses memory to maintain context and enables rich, one-on-one conversation flow.

📌 Features
✅ Transcript Extraction – Auto-fetches transcript from any YouTube video.

✅ Summarization Agent – Summarizes long transcripts into digestible context.

✅ Contextual QA Agent – Answers user queries based on video content or related topics.

✅ Conversational Memory – Maintains chat history for seamless back-and-forth interaction.

✅ Multi-Agent Workflow – Each agent performs a specialized task in sequence.

✅ Groq + LLaMA3 – Ultra-fast, low-latency LLM inference powered by Groq hardware.


🧠 Architecture

📘 Agent Overview
Agent	Role	Description
Transcript Agent	👂 Listener	Uses youtube_transcript_api to fetch captions from the YouTube URL.
Summarizer Agent	📄 Summarizer	Uses LLaMA3 to condense long transcripts into a summary.
QA Agent	🤖 Answerer	Uses LangChain's ConversationalRetrievalChain to answer based on vector DB and chat history.



🚀 How It Works
User inputs a YouTube URL

Transcript Agent fetches the transcript text.

Summarizer Agent condenses the transcript using LLaMA3.

Vector Store is built using FAISS for semantic search.

QA Agent runs a ConversationalRetrievalChain using the query, vector store, and memory.

🎯 Response is generated using context from both the video and previous messages.

