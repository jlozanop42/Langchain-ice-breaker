from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties1.linkedin import (
    scrape_linkedin_profile,
    scrape_linkedin_profile_with_curl_proxy,
)
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


def ice_break(name: str) -> str:
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    summary_template = """
             given the Linkedin information {information} about a person from I want you to create:
             1. a short summary
             2. two interesting facts about them
         """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile()
    # linkedin_data = scrape_linkedin_profile_with_curl_proxy(
    #    linkedin_profile_url=linkedin_profile_url
    # )

    print(chain.run(information=linkedin_data))


if __name__ == "__main__":
    print("Hello LangChain")
    ice_break("Sebastian Lozano Publicis Sapient")

# linkedin_data = scrape_linkedin_profile_with_curl_proxy(linkedin_profile_url="https://www.linkedin.com/in/nvaz/")
# print(linkedin_data)
