from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI


def get_response(data,query):

  #initilize the llm
  llm=OpenAI()

  agent=create_pandas_dataframe_agent(llm,data,verbose=True)

  return agent.run(query)