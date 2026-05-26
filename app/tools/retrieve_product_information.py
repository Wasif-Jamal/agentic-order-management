from app.agents.enquiry.retriever import Retriever


class RetrieveProductInformationTool:
    def __init__(self, retriever: Retriever):

        self.retriever = retriever

    def execute(self, query: str):

        return self.retriever.retrieve(query)
