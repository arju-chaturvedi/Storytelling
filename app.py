import streamlit as st
import sys
import os

# Enable imports from parent folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import custom modules
from utils.scraper import fetch_article_text, load_dummy_article
from models.summarizer import summarize_text
from utils.chunker import chunk_text
from utils.image_generator import generate_image_for_text

# App config
st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title("📰 AI-Powered News Summarizer")

# Input controls
use_dummy = st.checkbox("👨‍🔬 Use dummy article instead of scraping a URL")
url = st.text_input("Paste a news article URL:", "")
summary = None

# Load article
if use_dummy:
    article = load_dummy_article()
elif url:
    with st.spinner("Fetching article..."):
        article = fetch_article_text(url)
else:
    article = ""

# Show article and summary
if article:
    st.subheader("📄 Original Article")
    st.write(article)

    with st.spinner("Summarizing..."):
        summary = summarize_text(article)

    st.subheader("🧠 Summary (BART Model)")
    st.write(summary)
else:
    if not use_dummy and url:
        st.error("❌ Failed to fetch article. Please check the URL.")
    elif not use_dummy:
        st.info("Paste a URL or use the dummy article to begin.")

# Story slides
if summary:
    st.subheader("🧩 AI-Powered Story Slides")
    chunks = chunk_text(summary or article)

    for i, chunk in enumerate(chunks):
        st.markdown(f"### 📝 Slide {i + 1}")
        image_url = generate_image_for_text(chunk)
        st.image(image_url, use_container_width=True)
        st.write(chunk)
        st.markdown("---")
