import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()

st.title('GPT-3 Demo')
openai.api_key = os.getenv('OPENAI_API_KEY')
if not os.getenv('OPENAI_API_KEY'):
    st.error("OpenAI API key is required. Set the environment variable OPENAI_API_KEY.")
else:
    message = st.text_input("Question:")
    response = ""
    if message:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.0,
            messages=[
                {'role': 'user', 'content': message}
            ]
        ).choices[0]['message']['content']
    st.write(f"Response: {response}")