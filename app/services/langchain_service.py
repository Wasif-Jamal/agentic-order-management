from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

from app.agents.enquiry_agent import EnquiryAgent


class EnquiryChain:
    def __init__(self):

        self.enquiry_agent = EnquiryAgent()

        self.tools = {tool.name: tool for tool in (self.enquiry_agent.get_tools())}

        self.llm_with_tools = self.enquiry_agent.get_llm().bind_tools(
            self.enquiry_agent.get_tools()
        )

    def invoke(self, query: str):

        messages = [
            SystemMessage(content=(self.enquiry_agent.get_system_prompt())),
            HumanMessage(content=query),
        ]

        response = self.llm_with_tools.invoke(messages)

        messages.append(response)

        if response.tool_calls:
            for tool_call in response.tool_calls:
                tool_name = tool_call["name"]

                tool_args = tool_call["args"]

                tool = self.tools[tool_name]

                tool_result = tool.invoke(tool_args)

                messages.append(
                    ToolMessage(
                        content=str(tool_result), tool_call_id=(tool_call["id"])
                    )
                )

            final_response = self.llm_with_tools.invoke(messages)

            return final_response.content

        return response.content
