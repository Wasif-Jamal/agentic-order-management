from langchain_google_genai import ChatGoogleGenerativeAI

from app.config.env_config import settings

from app.prompts.prompt import ENQUIRY_AGENT_PROMPT

from app.tools.retrieve_product_information import retrieve_product_information


class EnquiryAgent:
    def __init__(self):

        self.system_prompt = ENQUIRY_AGENT_PROMPT

        self.tools = [retrieve_product_information]

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", google_api_key=(settings.GOOGLE_API_KEY)
        )

    def get_tools(self):

        return self.tools

    def get_llm(self):

        return self.llm

    def get_system_prompt(self):

        return self.system_prompt
