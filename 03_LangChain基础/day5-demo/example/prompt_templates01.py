from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder("msgs")
])
result = prompt_template.invoke({"msgs": [HumanMessage(content="hi!"), HumanMessage(content="how are you?")]})
print(result)