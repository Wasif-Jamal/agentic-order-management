from langchain_qdrant import QdrantVectorStore

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from qdrant_client import QdrantClient


class Retriever:

    def __init__(self):

        self.collection_name = (
            "product_knowledge_base"
        )

        self.qdrant_client = QdrantClient(
            host="localhost",
            port=6333
        )

        self.embedding_model = (
            HuggingFaceEmbeddings(
                model_name=(
                    "sentence-transformers/all-MiniLM-L6-v2"
                )
            )
        )

        self.vector_store = QdrantVectorStore(
            client=self.qdrant_client,
            collection_name=self.collection_name,
            embedding=self.embedding_model
        )

    def retrieve(
        self,
        query: str,
        limit: int = 3
    ):

        results = (
            self.vector_store.similarity_search(
                query=query,
                k=limit
            )
        )

        retrieved_chunks = [
            document.page_content
            for document in results
        ]

        return retrieved_chunks