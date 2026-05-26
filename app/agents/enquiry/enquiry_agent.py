from app.agents.enquiry.retriever import Retriever

from app.agents.enquiry.chain import EnquiryChain

from app.tools.retrieve_product_information import RetrieveProductInformationTool


class EnquiryAgent:
    def __init__(self):

        self.retriever = Retriever()

        self.retrieval_tool = RetrieveProductInformationTool(retriever=self.retriever)

        self.chain = EnquiryChain()

    def handle_query(self, query: str):

        retrieved_chunks = self.retrieval_tool.execute(query=query)

        context = "\n\n".join(retrieved_chunks)

        response = self.chain.invoke(context=context, question=query)

        return response
