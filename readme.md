# Project-CSV-Analyzer

## Introduction

In this project, we will explore a Python code snippet that allows us to analyze CSV files. We will discuss the key concepts behind the code, its structure, and provide code examples to illustrate its usage.

## Installation & create environment

Clone the project

```bash
  git clone link_to_copy
```

Go to the project directory

```bash
  cd proj_dir
```

Create the enviroment

```bash
  conda create --prefix ./lang_env
  conda activate {path}/lang_env
  python -m ipykernel install --user --name=lang_env
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Insert Open-ai api key

```bash
  touch .env
  insert your key as following: OPENAI_API_KEY=""
```

Start the server

```bash
  streamlit run app.py
```

## Code Explanation

Before diving into the code, let's briefly discuss the key concepts involved:

Streamlit: Streamlit is an open-source Python library that allows you to create interactive web applications for data analysis and visualization. It provides a simple and intuitive interface for building web-based data applications.

dotenv: dotenv is a Python library that loads variables from a .env file into the environment. It is commonly used to store sensitive information, such as API keys or database credentials, outside of the codebase.

Pandas: Pandas is a powerful data manipulation library in Python. It provides data structures and functions to efficiently analyze and manipulate structured data, such as CSV files.

get_response: get_response is a custom function that takes a Pandas DataFrame and a query as input and returns a response based on the query. This function is not provided in the code snippet but is referenced in the code.
The code is structured into a single function called get_response. This function takes two parameters: data and query. The data parameter represents the dataset on which the agent will operate, and the query parameter represents the query to be executed on the dataset.

### Detailed Explanation:

The code snippet is structured as follows:

Import the required libraries: streamlit, dotenv, and pandas. Additionally, import the get_response function from a custom module called utils.

Initialize the environment variables using load_dotenv(). This ensures that any variables defined in the .env file are available for use in the code.

Set the page configuration for the Streamlit application. This includes setting the page title and icon.

Display the title and header for the application using st.title and st.header functions, respectively.

Prompt the user to upload a CSV file using the st.file_uploader function. This allows the user to drag and drop a CSV file into the application.

Provide a text area for the user to enter a query using the st.text_area function.

Create a button labeled "Generate Response" using the st.button function.

If the "Generate Response" button is clicked, read the uploaded CSV file into a Pandas DataFrame using pd.read_csv.

Call the get_response function with the DataFrame and the user's query as input to obtain a response.

Display the DataFrame and the response using the st.write function.

get_response function:

Importing Required Libraries:

The code begins by importing the necessary libraries. We import the create_pandas_dataframe_agent function from the langchain_experimental.agents module. We also import the OpenAI class from the langchain.llms module.
Initializing the LLM:

Next, we initialize the LLM by creating an instance of the OpenAI class and assigning it to the llm variable.
Creating a Pandas Dataframe Agent:

We then create a Pandas Dataframe Agent by calling the create_pandas_dataframe_agent function. This function takes three parameters: the LLM instance (llm), the dataset (data), and an optional verbose parameter to enable verbose output. The function returns an agent object, which we assign to the agent variable.
Running the Query:

Finally, we run the query on the agent by calling the run method of the agent object and passing the query parameter. The method processes the query using the LLM and returns the response.

## libraries

```
import streamlit as st
from dotenv import load_dotenv
import pandas as pd
from utils import get_response
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
```

## Conclusion

In this project, we explored a Python code that allows us to analyze CSV files using the Streamlit library. We discussed the key concepts behind the code, its structure, and provided code examples to illustrate its usage. By leveraging this code, you can easily build interactive web applications for CSV analysis.
