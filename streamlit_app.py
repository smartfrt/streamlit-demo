import streamlit as st
from openai import OpenAI

st.title("Hi there!")

# Open the .env file, and read in the api key into a variable
with open(".env", "r") as file:
    open_ai_api_key = file.read()

client = OpenAI(
    api_key = open_ai_api_key
)

chat_history = [
    {"role": "system", "content": "Please translate all user input into Chinese."}
]

# user_input = "I need some help with writing a letter to my professor. Can you help me with that?"
user_input = st.text_input("Enter your message: ")
chat_history.append({"role": "user", "content": user_input})

# sending a request to OpenAI through the OpenAI API
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=chat_history, 
    temperature=0
)

currResponse = response.choices[0].message.content
chat_history.append({"role": "assistant", "content": currResponse})
st.write(currResponse)

