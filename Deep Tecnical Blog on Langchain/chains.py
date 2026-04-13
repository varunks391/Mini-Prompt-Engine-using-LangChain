from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(model="gpt-4o-mini")

template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic}"
)

chain = LLMChain(llm=llm, prompt=template)

print(chain.run("LangChain"))
