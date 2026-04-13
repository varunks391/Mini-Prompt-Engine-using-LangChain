from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-4o-mini")

memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory)

conversation.run("Hi, I'm Varun")
print(conversation.run("What is my name?"))
