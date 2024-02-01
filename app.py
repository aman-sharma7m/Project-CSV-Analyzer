import streamlit as st 
from dotenv import load_dotenv
import pandas as pd
from utils import get_response

#initialize the keys
load_dotenv()


st.set_page_config(page_title='csv anaylzer',page_icon='😎')
st.title('Lets do some analysis on CSV')
st.header('Please upload your file here:')
file=st.file_uploader('Drag and drop your file here',type='csv')
query=st.text_area('Enter Your query ')
submit=st.button('Generate Response')

if submit:
  data=pd.read_csv(file)
  response=get_response(data,query)
  st.write(data)
  st.write(response)