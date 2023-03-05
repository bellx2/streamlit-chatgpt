import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()

st.title('GPT-3 Demo')
openai.api_key = os.getenv('OPENAI_API_KEY')
if not os.getenv('OPENAI_API_KEY'):
    st.error("OpenAI API key が必要です。環境変数 OPENAI_API_KEY を設定してください。")
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