import json


class Evaluator:
    def __init__(self, search_engine):
        self.search_engine = search_engine

    def precision_at_k(self, query, relevant_docs, k=5):
        """
        relevant_docs: list of doc_ids considered relevant
        """
        results = self.search_engine.search(query, top_k=k)
        retrieved_docs = [doc_id for doc_id, _ in results]

        relevant_retrieved = len(
            set(retrieved_docs).intersection(set(relevant_docs))
        )

        return relevant_retrieved / k if k > 0 else 0