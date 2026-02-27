import json
from collections import defaultdict
from src.preprocessing.tokenizer import tokenize


class SearchEngine:
    def __init__(self, inverted_index_path, idf_path, documents_path):
        self.inverted_index = self.load_json(inverted_index_path)
        self.idf_scores = self.load_json(idf_path)
        self.documents = self.load_json(documents_path)

    def load_json(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def search(self, query, top_k=5):
        tokens = tokenize(query)

        scores = defaultdict(float)

        for token in tokens:
            if token in self.inverted_index:
                for doc_id, tf in self.inverted_index[token].items():
                    scores[doc_id] += tf * self.idf_scores.get(token, 0)

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        return ranked[:top_k]

    def get_document(self, doc_id):
        index = int(doc_id.split("_")[1])
        return self.documents[index]
    
    def boolean_search(self, query):
        tokens = query.upper().split()
    
        result_sets = []
    
        i = 0
        while i < len(tokens):
            token = tokens[i]
    
            if token in ("AND", "OR"):
                i += 1
                continue
    
            postings = set(self.inverted_index.get(token.lower(), {}).keys())
            result_sets.append(postings)
    
            i += 1
    
        if "AND" in tokens:
            result = set.intersection(*result_sets)
        elif "OR" in tokens:
            result = set.union(*result_sets)
        else:
            result = result_sets[0] if result_sets else set()
    
        return list(result)