from typing import Tuple

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from output_parsers import person_intel_parser, PersonIntel
from third_parties1.linkedin import (
    scrape_linkedin_profile,
    scrape_linkedin_profile_with_curl_proxy,
)
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


def ice_break(name: str) -> Tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    summary_template = """
             given the Linkedin information {information} about a person from I want you to create:
             1. a short summary
             2. two interesting facts about them
             3. A topic that may interest them
             4. 2 creative ice breakers to open a conversation with them
                     \n{format_instructions}
         """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )
    # We are parsing the output with the format instructions variable
    # The get_format_instructions method is from Pydantic

    llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile()
    # linkedin_data = scrape_linkedin_profile_with_curl_proxy(
    #    linkedin_profile_url=linkedin_profile_url
    # )

    result = chain.run(information=linkedin_data)
    print(result)

    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Hello LangChain")
    ice_break("Sebastian Lozano Publicis Sapient")

# linkedin_data = scrape_linkedin_profile_with_curl_proxy(linkedin_profile_url="https://www.linkedin.com/in/nvaz/")
# print(linkedin_data)
