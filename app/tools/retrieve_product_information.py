from langchain_core.tools import tool

from app.tools.retriever import Retriever


retriever = Retriever()


@tool
def retrieve_product_information(query: str) -> str:
    """
    Retrieve product information
    from vector database.
    """

    results = retriever.retrieve(query)

    return "\n\n".join(results)
