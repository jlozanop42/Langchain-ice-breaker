from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                        Your answer should contain only a URL"""
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to get the Linkedin page URL",
        )
    ]
    # name must be unique between all the tools, function is the function that the LLM will invoque
    # when decide to use that tool.Description it's optional but recommended because the agent when deciding
    # whether to use the tool or not it's going to use the description to decide

    agent = initialize_agent(
        tools=tools_for_agent,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm=llm,
        verbose=True,
    )
    # AgentType is super important because it will decide what is the reasoning process that the agent is going
    # to make once it needs to perform a taskl. Different agent type will lead to different results
    # Verbose it's crucial when defining an agent. We are saying the agent that we want verbose logs
    # after every task/step
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    return linkedin_profile_url
