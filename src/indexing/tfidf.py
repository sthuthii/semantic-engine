import json
import math
import os
import token
from typing import Dict, List
from collections import defaultdict

class TFIDFBuilder:
    def __init__(self, inverted_index, total_docs):
        self.inverted_index = inverted_index
        self.total_docs = total_docs
        self.idf_scores = {}

    def compute(self):
        for term, postings in self.inverted_index.items():
            df = len(postings)
            self.idf_scores[term] = math.log(self.total_docs/(1+df))
    
    def save_idf(self,path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.idf_scores, f, indent=2)

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def rank_query(query, inverted_index, idf_scores):
    """
    Ranking the query based on the TF-IDF score

    """
    from src.preprocessing.tokenizer import tokenize

    tokens = tokenize(query)
    scores = defaultdict(float)

    for token in tokens:
        if token in inverted_index:
            for doc_id, tf in inverted_index[token].items():
                scores[doc_id] += tf * idf_scores.get(token, 0)
    
    ranked_results = sorted(scores.items(), key=lambda x : x[1], reverse=True)
    return ranked_results[:5]

if __name__=="__main__":
    INVERTED_PATH = "data/processed/inverted_index.json"

    inverted_index = load_json(INVERTED_PATH)
    total_docs = len({term for postings in inverted_index.values() for term in postings})

    tf = TFIDFBuilder(inverted_index, total_docs)
    tf.compute()
    tf.save_idf("data/processed/idf_scores.json")
    print(f"IDF SCORING COMPLETE")

    results = rank_query("binary tree traversal", inverted_index, tf.idf_scores)
    print("\nTop Results:")
    for doc_id, score in results:
        print(doc_id, score)



