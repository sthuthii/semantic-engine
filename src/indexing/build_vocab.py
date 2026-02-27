import json
import os
from collections import defaultdict
from typing import Dict
from src.preprocessing.tokenizer import tokenize


class VocabularyBuilder:
    def __init__(self):
        self.vocabulary = set()
        self.term_frequencies: Dict[str, Dict[str, int]] = {}

    def process_documents(self, documents):
        for idx, doc in enumerate(documents):
            doc_id = f"doc_{idx}"

            tokens = tokenize(doc.get("content", ""))

            tf = defaultdict(int)

            for token in tokens:
                tf[token] += 1
                self.vocabulary.add(token)

            self.term_frequencies[doc_id] = dict(tf)

    def save(self, vocab_path, tf_path):
        os.makedirs(os.path.dirname(vocab_path), exist_ok=True)

        with open(vocab_path, "w", encoding="utf-8") as f:
            json.dump(sorted(list(self.vocabulary)), f, indent=2)

        with open(tf_path, "w", encoding="utf-8") as f:
            json.dump(self.term_frequencies, f, indent=2)


def load_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    INPUT_PATH = "data/raw/raw_documents.json"
    VOCAB_PATH = "data/processed/vocabulary.json"
    TF_PATH = "data/processed/term_frequencies.json"

    documents = load_documents(INPUT_PATH)

    builder = VocabularyBuilder()
    builder.process_documents(documents)
    builder.save(VOCAB_PATH, TF_PATH)

    print(f"Documents processed: {len(documents)}")
    print(f"Vocabulary size: {len(builder.vocabulary)}")