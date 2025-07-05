import streamlit as st
from st_chat_message import message
from openai import OpenAI

# "with": wait for the operation to finish
with open(".env", "r") as file:
    open_ai_api_key = file.read()

client = OpenAI(
    api_key = open_ai_api_key
)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        {"role": "system", "content": "Please translate all user input into Chinese."}
    ]

# print all messages
for chat_message in st.session_state["chat_history"]:
    # check if it's the user's chat message
    # If so, create a "user message" element
    if chat_message["role"] == "user" and chat_message["content"] != "":
        message(chat_message["content"], is_user=True)
    elif chat_message["role"] == "assistant":
        message(chat_message["content"])
    else:
        continue

with st.form("input"):
    user_message = st.text_input("Please enter your message: ")
    submitted_btn = st.form_submit_button('Submit')
    if submitted_btn and user_message != "":
        st.session_state["chat_history"].append({"role": "user", "content": user_message})

        # sending a message to OpenAI through the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=st.session_state["chat_history"], 
            temperature=0
        )
        chatgpt_message = response.choices[0].message.content
        st.session_state["chat_history"].append({"role": "assistant", "content": chatgpt_message})

        # refresh our screen
        st.rerun()
    



