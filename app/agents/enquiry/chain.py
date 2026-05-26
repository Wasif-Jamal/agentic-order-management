from langchain_core.prompts import PromptTemplate

from langchain_google_genai import ChatGoogleGenerativeAI

from app.config.env_config import settings

from app.agents.enquiry.prompts import ENQUIRY_PROMPT


class EnquiryChain:
    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model="gemma-4-26b-a4b-it", google_api_key=(settings.GOOGLE_API_KEY)
        )

        self.prompt = PromptTemplate(
            template=ENQUIRY_PROMPT, input_variables=["context", "question"]
        )

        self.chain = self.prompt | self.llm

    def invoke(self, context: str, question: str):

        response = self.chain.invoke({"context": context, "question": question})

        return response.content
