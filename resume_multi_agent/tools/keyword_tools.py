import re

def extract_keywords(text: str) -> list:
    """
    Extract keywords from text.
    """
    words = re.findall(r"[A-Za-z]{4,}", text.lower())
    stopwords = {
        "with","that","this","have","from","your",
        "will","into","about","which","their"
    }

    keywords = [w for w in words if w not in stopwords]
    return list(set(keywords))
