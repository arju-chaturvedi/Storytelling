import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def chunk_text(text, max_words=60):
    doc = nlp(text)
    chunks = []
    chunk = ""

    for sent in doc.sents:
        if len(chunk.split()) + len(sent.text.split()) <= max_words:
            chunk += " " + sent.text.strip()
        else:
            chunks.append(chunk.strip())
            chunk = sent.text.strip()

    if chunk:
        chunks.append(chunk.strip())

    return chunks
