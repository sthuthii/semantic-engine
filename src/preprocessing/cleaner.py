import re
import json

def remove_citations(text):
    """
    Remove citations from the text
    
    """
    return re.sub(r"\[\d+\]", "", text) #remove citations

def normalize_whitespace(text):
    """
    Normalizing whitespace
    
    """
    return re.sub(r"\s+", " ", text).strip()

def clean_text(text):
    """
    Full cleaning pipeline

    """
    text = text.lower()  #convert to lowercase
    text = remove_citations(text)
    text = normalize_whitespace(text)
    return text

def cleaned_document(input_document):

    cleaned_document= []
    """
    Clean a single document and return the cleaned version."""

    for doc in input_document: 
        cleaned_content = clean_text(doc['content'])
        cleaned_document.append({
            "url" : doc['url'],
            "title": doc['title'].lower().strip(),
            'content' : cleaned_content
        })

    return cleaned_document
    
if __name__ == "__main__":
    with open('data/raw/raw_documents.json', 'r', encoding='utf-8') as f:
        documents = json.load(f)

        if isinstance(documents, dict):
            documents = [documents]

        cleaned = cleaned_document(documents)

    with open('data/processed/processed_documents.json', "w", encoding='utf-8') as f:
        json.dump(cleaned, f, indent=2)

    print(f"Cleaned {len(cleaned)} documents.")

    