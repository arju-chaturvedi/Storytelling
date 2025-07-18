from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    summary = summarizer_pipeline(text, max_length=400, min_length=120, do_sample=False)
    return summary[0]['summary_text']
