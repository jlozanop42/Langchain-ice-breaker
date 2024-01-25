from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.linkedin import scrape_linkedin_profile_with_curl_proxy

information = """
Samuel Benjamin Bankman-Fried[2] (born March 5, 1992), or SBF,[3] is an American entrepreneur who was convicted of fraud and related crimes in November 2023. Bankman-Fried founded the FTX cryptocurrency exchange and was celebrated as a "poster boy" for crypto.[4] At the peak of his success, he was ranked the 41st-richest American in the Forbes 400.[5]

The public persona of Bankman-Fried masked significant problems at FTX, and in November 2022 when evidence of potential fraud began to surface, depositors quickly withdrew their assets, forcing the company into bankruptcy. On December 12, 2022, Bankman-Fried was arrested in the Bahamas and extradited to the United States, where he was indicted on seven criminal charges including wire fraud, commodities fraud, securities fraud, money laundering, and campaign finance law violations.[6][7][8]

On November 2, 2023, in the case of United States v. Bankman-Fried, he was convicted of all seven counts of fraud, conspiracy, and money laundering.[9] His sentencing, where experts say he faces decades in prison,[10][11] is scheduled for March 28, 2024.[12]
"""

if __name__ == '__main__':
     print('Hello Langchain')

     # summary_template = """
     #     given the information {information} about a person from I want you to create
     #     1. a short summary
     #     2. two interesting facts about them
     # """
     #
     # summary_prompt_template = PromptTemplate(input_variables = ["information"], template = summary_template)
     #
     # llm = ChatOpenAI(temperature = 0, model_name = "gpt-3.5-turbo")
     #
     # chain = LLMChain(llm = llm, prompt = summary_prompt_template)
     #
     # print(chain.run(information=information))

sebastian_data = scrape_linkedin_profile()
print(sebastian_data.json())

#linkedin_data = scrape_linkedin_profile_with_curl_proxy(linkedin_profile_url="https://www.linkedin.com/in/nvaz/")
#print(linkedin_data)
