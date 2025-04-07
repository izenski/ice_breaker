# import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

information = """
Joan Ruth Bader Ginsburg; née Bader; March 15, 1933 - September 18, 2020) was 
an American lawyer and jurist 
who served as an associate justice of the Supreme Court of the United States 
from 1993 until her death in 2020.  
She was nominated by President Bill Clinton to replace retiring justice Byron 
White, and at the time was viewed 
as a moderate consensus-builder.  Ginsburg was the first Jewish woman and the 
second woman to serve on the Court, 
after Sandra Day O'Connor. During her tenure, Ginsburg authored the majority 
opinions in cases such as United States 
v. Virginia (1996), Olmstead v. L.C. (1999), Friends of the Earth, Inc. v. 
Laidlaw Environmental Services, Inc. (2000), 
and City of Sherrill v. Oneida Indian Nation of New York (2005). Later in her 
tenure, Ginsburg received attention for 
passionate dissents that reflected liberal views of the law. She was popularly 
dubbed "the Notorious R.B.G.",[a] a 
moniker she later embraced.
"""

if __name__ == "__main__":
    print("Hello langChain")
    # print(os.environ['OPENAI_API_KEY'])

    summary_template = """
        given the information {information} about a person
         I want you to create:
        1. A one sentence summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    # llm = ChatOllama(model="mistral")
    llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": information})

    print(res)
    # chain = summary_prompt_template.combine(llm)
