import json
import os
from collections import defaultdict
from typing import Dict

class InvertedIndexBuilder:
    def __init__(self):
        self.inverted_index : Dict[str , Dict[str,int]] = defaultdict(dict)

    def build(self, term_frequencies: Dict[str , Dict[str,int]]):
        for doc_id, terms in term_frequencies.items():
            for term,freq in terms.items():
                self.inverted_index[term][doc_id] = freq
    

    def save(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.inverted_index, f, indent=2)


def load_frequencies(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    

if __name__=="__main__":
    TF_PATH = "data/processed/term_frequencies.json"
    OUTPUT_PATH = "data/processed/inverted_index.json"

    term_frequency = load_frequencies(TF_PATH)
    builder = InvertedIndexBuilder()
    builder.build(term_frequency)
    builder.save(OUTPUT_PATH)
    print(f"The total number number of unqiue terms indexed: {len(builder.inverted_index)}")

    
