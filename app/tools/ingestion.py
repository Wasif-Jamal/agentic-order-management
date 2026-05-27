from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


class Ingestion:
    def __init__(self):

        self.collection_name = "product_knowledge_base"

        self.qdrant_client = QdrantClient(host="localhost", port=6333)

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, chunk_overlap=100
        )

    def create_collection(self):

        collections = self.qdrant_client.get_collections()

        existing_collections = [
            collection.name for collection in collections.collections
        ]

        if self.collection_name in (existing_collections):
            return

        self.qdrant_client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

    def ingest(self):

        self.create_collection()

        loader = PyPDFLoader("data/agentic_order_management_knowledge_base.pdf")

        documents = loader.load()

        chunked_documents = self.text_splitter.split_documents(documents)

        vector_store = QdrantVectorStore(
            client=self.qdrant_client,
            collection_name=self.collection_name,
            embedding=self.embedding_model,
        )

        vector_store.add_documents(documents=chunked_documents)

        print("Knowledge base ingestion completed.")


if __name__ == "__main__":
    ingestion = Ingestion()

    ingestion.ingest()
