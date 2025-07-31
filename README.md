This is a **multi-agent conversational AI application** powered by **[LLaMA3 via Groq API]** and **[LangChain]**, designed to **extract**, **summarize**, and **interact** with YouTube videos intelligently. It enables rich, one-on-one conversations while maintaining contextual memory and fast responses using Groq hardware.

---
<img width="1536" height="1024" alt="ChatGPT Image Jul 31, 2025, 06_54_08 PM" src="https://github.com/user-attachments/assets/85811293-13a2-4c42-9422-111187ebd326" />

---

## 📌 Features

- ✅ **Transcript Extraction** – Auto-fetches transcript from any YouTube video.
- ✅ **Summarization Agent** – Summarizes long transcripts into digestible chunks.
- ✅ **Contextual QA Agent** – Answers user queries based on video content.
- ✅ **Conversational Memory** – Maintains chat history for seamless interaction.
- ✅ **Multi-Agent Workflow** – Agents work sequentially to perform specific tasks.
- ✅ **Groq + LLaMA3** – Ultra-fast, low-latency LLM inference powered by Groq.

---

## 🧠 Architecture

### 🧩 Agent Overview

| Agent            | Role        | Description                                                                 |
|------------------|-------------|-----------------------------------------------------------------------------|
| Transcript Agent | 👂 Listener | Uses `youtube_transcript_api` to fetch captions from a YouTube URL.        |
| Summarizer Agent | 📄 Summarizer | Uses LLaMA3 via Groq to summarize long transcripts.                         |
| QA Agent         | 🤖 Answerer | Uses LangChain's `ConversationalRetrievalChain` to answer contextually.    |

---

## 🚀 How It Works

1. **User inputs a YouTube URL**
2. 🧠 **Transcript Agent** fetches the transcript using `youtube_transcript_api`.
3. 📄 **Summarizer Agent** condenses the transcript using LLaMA3 (via Groq API).
4. 🗂️ **Vector Store** is built using **FAISS** for semantic search on transcript content.
5. 🤖 **QA Agent** uses **ConversationalRetrievalChain** to generate responses based on:
   - The query
   - Vector database (semantic context)
   - Chat memory (for continuity)
6. ✨ **Response is generated** with full context from video and conversation history.

---



