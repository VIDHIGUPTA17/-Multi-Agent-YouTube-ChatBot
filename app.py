# import streamlit as st
# from FetchYouTubedata import get_transcript, summarize_text
# from QA import build_vector_store, answer_question
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.runnables import RunnableParallel, RunnablePassthrough
# from langchain.chains import ConversationalRetrievalChain

# # --- App Title ---
# st.title("🎥 Multi-Agent YouTube ChatBot (Groq + LLaMA3)")

# # --- YouTube Input ---
# video_url = st.text_input("Enter YouTube Video URL")

# if video_url:
#     # --- Step 1: Transcript Agent ---
#     with st.spinner("Fetching transcript..."):
#         transcript = get_transcript(video_url)
#     st.success("Transcript fetched!")

#     # --- Step 2: Summarizer Agent ---
#     with st.spinner("Summarizing..."):
#         summary = summarize_text(transcript)
#     st.write("📄 **Summary:**")
#     st.info(summary)

#     # --- Step 3: Build Vector Store for Retrieval ---
#     with st.spinner("Preparing knowledge base..."):
#         vectordb = build_vector_store(transcript)

#     # --- Step 4: Chat with Agent ---
#     st.divider()
#     st.subheader("💬 Chat with Multi-Agent AI")

#     # Initialize chat history
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []

#     # LLaMA 3 Model via Groq
#     llm = ChatGroq(temperature=0.3, model_name="llama3-8b-8192")

#     # Retrieval chain
#     qa_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=vectordb.as_retriever(search_type="similarity", k=3),
#         return_source_documents=False,
#     )

#     # Input box
#     user_query = st.chat_input("Ask about the video or related topic...")

#     if user_query:
#         # Add user message
#         st.chat_message("user").markdown(user_query)

#         # Run multi-agent logic
#         try:
#             result = qa_chain({
#                 "question": user_query,
#                 "chat_history": st.session_state.chat_history
#             })

#             # Extract AI response
#             answer = result["answer"]

#             # Save to history
#             st.session_state.chat_history.append((user_query, answer))

#             # Show AI response
#             with st.chat_message("assistant"):
#                 st.markdown(answer)

#         except Exception as e:
#             st.error(f"❌ Error: {e}")


# import streamlit as st
# from FetchYouTubedata import get_transcript, summarize_text
# from QA import build_vector_store, answer_question
# from langchain_core.messages import AIMessage, HumanMessage
# from langchain_groq import ChatGroq
# from langchain.chains import ConversationalRetrievalChain

# # --- App Title ---
# st.title("🎥 Multi-Agent YouTube ChatBot (Groq + LLaMA3)")

# # --- YouTube Input ---
# video_url = st.text_input("Enter YouTube Video URL")

# if video_url:
#     # --- Step 1: Transcript Agent ---
#     with st.spinner("Fetching transcript..."):
#         transcript = get_transcript(video_url)
#     st.success("Transcript fetched!")

#     # --- Step 2: Summarizer Agent ---
#     with st.spinner("Summarizing..."):
#         summary = summarize_text(transcript)
#     st.write("📄 **Summary:**")
#     st.info(summary)

#     # --- Step 3: Build Vector Store for Retrieval ---
#     with st.spinner("Preparing knowledge base..."):
#         vectordb = build_vector_store(transcript)

#     # --- Step 4: Chat with Agent ---
#     st.divider()
#     st.subheader("💬 Chat with Multi-Agent AI")

#     # Initialize chat memory using LangChain messages
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []

#     # LLaMA 3 Model via Groq
#     llm = ChatGroq(temperature=0.3, model_name="llama3-8b-8192")

#     # Retrieval chain with memory
#     qa_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=vectordb.as_retriever(search_type="similarity", k=3),
#         return_source_documents=False,
#     )

#     # Input box
#     user_query = st.chat_input("Ask about the video or related topic...")

#     if user_query:
#         # Display user message
#         st.chat_message("user").markdown(user_query)

#         # Construct history in required format
#         history_messages = []
#         for msg in st.session_state.chat_history:
#             history_messages.append(HumanMessage(content=msg["user"]))
#             history_messages.append(AIMessage(content=msg["ai"]))

#         # Run multi-agent logic with memory
#         try:
#             result = qa_chain({
#                 "question": user_query,
#                 "chat_history": history_messages
#             })

#             answer = result["answer"]

#             # Display AI response
#             with st.chat_message("assistant"):
#                 st.markdown(answer)

#             # Update session memory
#             st.session_state.chat_history.append({
#                 "user": user_query,
#                 "ai": answer
#             })

#         except Exception as e:
#             st.error(f"❌ Error: {e}")



import streamlit as st
from FetchYouTubedata import get_transcript, summarize_text
from QA import build_vector_store, answer_question
from langchain_core.messages import AIMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain

# --- App Title ---
st.title("🎥 Multi-Agent YouTube ChatBot (Groq + LLaMA3)")

# --- YouTube Input ---
video_url = st.text_input("Enter YouTube Video URL")

if video_url:
    # Step 1: Transcript Agent
    with st.spinner("Fetching transcript..."):
        transcript = get_transcript(video_url)
    st.success("✅ Transcript fetched!")

    # Step 2: Summarizer Agent
    with st.spinner("Summarizing transcript..."):
        summary = summarize_text(transcript)
    st.write("📄 **Video Summary:**")
    st.info(summary)

    # Step 3: Build Vector Store
    with st.spinner("Building knowledge base..."):
        vectordb = build_vector_store(transcript)
    st.success("✅ Knowledge base ready!")

    # Step 4: Initialize Chat
    st.divider()
    st.subheader("💬 Chat with Multi-Agent AI")

    # Chat memory stored in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Initialize Groq + LLaMA 3 model
    llm = ChatGroq(
        temperature=0.3,
        model_name="llama3-8b-8192"
    )

    # Conversational QA chain with memory
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever(search_type="similarity", k=3),
        return_source_documents=False
    )

    # --- Chat Interface ---
    user_input = st.chat_input("Ask about the video or related topic...")

    if user_input:
        # Display user message
        st.chat_message("user").markdown(user_input)

        # Reconstruct chat history for model
        history_messages = []
        for turn in st.session_state.chat_history:
            history_messages.append(HumanMessage(content=turn["user"]))
            history_messages.append(AIMessage(content=turn["ai"]))

        # Get model response
        try:
            response = qa_chain({
                "question": user_input,
                "chat_history": history_messages
            })

            answer = response["answer"]

            # Display AI response
            with st.chat_message("assistant"):
                st.markdown(answer)

            # Save turn in memory
            st.session_state.chat_history.append({
                "user": user_input,
                "ai": answer
            })

        except Exception as e:
            st.error(f"❌ Error: {e}")
