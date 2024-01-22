import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def perform_llm_prompt_request(assistant_message: str, user_prompt: str) -> str:
    max_tokens = 650
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    llm = ChatOpenAI(
        openai_api_key=openai_api_key,
        model="gpt-4-1106-preview",
        temperature=0.1,
        max_tokens=max_tokens,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", assistant_message),
            ("user", "{input}"),
        ]
    )

    chain = prompt | llm
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    llm_answer = chain.invoke({"input": user_prompt}).split(',')

    return llm_answer
