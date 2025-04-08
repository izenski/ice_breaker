from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain.chains import LLMChain
from dotenv import load_dotenv
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser

from linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    summary_template = """
        given the information {information} about a person
         I want you to create:
        1. A one sentence summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm 
    linkedin_data: str = scrape_linkedin_profile(linkedin_profile_url="whatever")
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
    # chain = summary_prompt_template.combine(llm)
