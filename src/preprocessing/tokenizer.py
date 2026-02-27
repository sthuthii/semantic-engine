import re
from typing import List


# Expandable stopword list
STOPWORDS = {
    "the", "is", "in", "at", "of", "and", "a", "to",
    "for", "on", "with", "as", "by", "an", "be",
    "this", "that", "from", "or", "are", "was",
    "it", "which", "can", "has", "have", "will"
}

def tokenize(text: str) -> List[str]:
    """
    Tokenize the input text into a list of words.
    
    Args:
        text (str): The input text to tokenize.
        
    Returns:
        List[str]: A list of tokens extracted from the input text.
    """
    # Use regular expressions to find words, ignoring punctuation
    if not text:
        return []
    
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ",text).strip()

    tokens = text.split()

    filtered_tokens = [
        token for token in tokens if token not in STOPWORDS
    ]

    return filtered_tokens