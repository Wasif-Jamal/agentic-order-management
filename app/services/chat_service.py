from app.services.langchain_service import EnquiryChain


class ChatService:
    def __init__(self):

        self.enquiry_chain = EnquiryChain()

    def process_query(self, query: str) -> str:

        response = self.enquiry_chain.invoke(query=query)

        return str(response)
