import requests
from bs4 import BeautifulSoup

def fetch_article_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: Status {response.status_code} for URL: {url}")
            return ""

        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text(strip=True) for p in paragraphs])
        return article_text.strip()

    except Exception as e:
        print(f"❌ Exception during scraping: {e}")
        return ""

def load_dummy_article():
    return """
    Artificial intelligence is rapidly transforming journalism. With the ability to generate summaries,
    draft headlines, and even create entire articles, AI tools are becoming essential in modern newsrooms.
    However, journalists and editors must balance automation with editorial integrity, ensuring that facts
    are checked and context is preserved. As AI models improve, they may also help detect fake news and
    provide multilingual content more efficiently.

    Newsrooms must also decide how to present AI-generated content transparently. Readers should be aware
    when articles or parts of them are produced using algorithms. With appropriate checks in place, AI
    could assist with breaking news updates, analysis of large datasets, and even personalized news delivery.

    But the future of journalism with AI will depend not just on technology, but on the people who guide
    its use responsibly.
    """
