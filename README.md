# 📰 AI-Powered News Summarizer with Slide Generator

An interactive Streamlit app that scrapes news articles, summarizes them using a Transformer-based model (BART), and generates visually engaging slides with images — designed for nonlinear storytelling.

---

## 🔍 Features

- 📄 Scrape news articles from a URL or use a dummy article
- 🧠 Summarize long text with a HuggingFace BART model
- 🧩 Automatically split text into story slides
- 🖼️ Generate random, relevant images (Wikimedia/Unsplash)
- 🧪 Built with modular Python structure (`utils`, `models`, `app`)

---

## 📸 Demo Preview

| Summary Output | Slide Generator |
|----------------|-----------------|
| ![summary](https://via.placeholder.com/300x150?text=Summary+Demo) | ![slides](https://via.placeholder.com/300x150?text=Slide+View) |

*(Replace with your own screenshots)*

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/reimagining-journalism-with-ai.git
cd reimagining-journalism-with-ai
pip install -r requirements.txt
streamlit run app/app.py
