

from langchain_google_genai import  ChatGoogleGenerativeAI

import streamlit as st

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp" , api_key="AIzaSyAO-imGsbJJZM418mONCiQo2Dufzqd8bMs") #it will load the model and api key

st.title("AI Generated Information")

user_input = st.text_input("Write Something") #it will take the input from the user

if user_input:
    response = llm.invoke(user_input)
    st.write(response.content) #it will generate the response

