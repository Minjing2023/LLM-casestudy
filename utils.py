import os

os.environ["OPENAI_API_KEY"] = ""

from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from casestudy_model import CaseStudy
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=openai_api_key)
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]


def generate_casestudy(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    output_parser = PydanticOutputParser(pydantic_object=CaseStudy)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result

#print(generate_casestudy("Jack, operation accounting, manager", os.getenv("OPENAI_API_KEY")))
