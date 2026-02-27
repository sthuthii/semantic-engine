from src.retrieval.search_engine import SearchEngine
from src.evaluation.metrics import Evaluator

def main():
    engine = SearchEngine(
        inverted_index_path="data/processed/inverted_index.json",
        idf_path="data/processed/idf_scores.json",
        documents_path="data/raw/raw_documents.json"
    )

    evaluator = Evaluator(engine)
    precision = evaluator.precision_at_k(
    query="binary tree",
    relevant_docs=["doc_0", "doc_3"],
    k=5
)

    print("Precision@5:", precision)

    print("DSA Search Engine")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("search > ")

        if query.lower() == "exit":
            break

        results = engine.search(query)

        if not results:
            print("No results found.\n")
            continue

        for doc_id, score in results:
            doc = engine.get_document(doc_id)

            print(f"\nTitle: {doc['title']}")
            print(f"Score: {round(score, 3)}")
            print(f"URL: {doc['url']}")
            print("-" * 50)

        print("\n")


if __name__ == "__main__":
    main()


