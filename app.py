# app.py

import streamlit as st
from summarizer import extract_video_id, get_transcript, load_summarizer, summarize_text

st.set_page_config(
    page_title="🎬 YouTube Summarizer",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "This is a simple YouTube summarizer app using Streamlit and HuggingFace."
    }
)

# Toggle for theme
st.markdown("""
    <style>
        body { background-color: #121212; color: #ffffff; }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            transition: 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .summary-box {
            border: 2px solid #4CAF50;
            padding: 15px;
            border-radius: 10px;
            background-color: #1e1e1e;
        }
        .heading {
            font-size: 2.5em;
            color: #4CAF50;
            text-align: center;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='heading'>YouTube Video Summarizer 📽️</div>", unsafe_allow_html=True)

st.write("### 🔗 Enter a YouTube URL and get a summarized transcript of the video.")

url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("✨ Summarize Video"):
    if url:
        with st.spinner("⏳ Fetching transcript and summarizing..."):
            try:
                video_id = extract_video_id(url)
                transcript = get_transcript(video_id)
                summarizer = load_summarizer()
                summary = summarize_text(transcript, summarizer)

                st.success("✅ Summary Generated!")
                st.markdown(f"""
                    <div class='summary-box'>
                        <strong>Summary:</strong><br>{summary}
                    </div>
                """, unsafe_allow_html=True)

                with st.expander("📜 Full Transcript"):
                    st.write(transcript)

            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid YouTube video URL.")
