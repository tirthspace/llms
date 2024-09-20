import streamlit as st
import client

st.title("GPT Clone Bot")

with st.sidebar:
    model = st.radio(
        "Choose model",
        ["gemma2", "qwen2.5", "phi3.5", "llama2"],
        captions=[
            "2B params (*fastest*)",
            "3B params",
            "3B params",
            "7B params",
        ]
    )

def get_response(model, input_text):
    if model == "llama2":
        response = client.get_llama2_response(input_text)
        return response
    elif model == "gemma2":
        response = client.get_gemma2_response(input_text)
        return response
    elif model == "qwen2.5":
        response = client.get_qwen25_response(input_text)
        return response
    elif model == "phi3.5":
        response = client.get_phi35_response(input_text)
        return response

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=message["avatar"]):
        st.markdown(message["content"])

# User input
input_text = st.chat_input("How can I help you?")

if input_text:
    # Add user message to chat history
    st.session_state.messages.append({
        "role":"user",
        "content":input_text,
        "avatar":"🐻"
    })

    # Show user message 
    with st.chat_message("You", avatar="🐻"):
        st.markdown(input_text)


    # Bot response
    message =  st.chat_message("Bot", avatar="🤖")
    response = get_response(
                    model,
                    f"{st.session_state.messages}"
                    )

    message.write(response)
    st.session_state.messages.append({"role": "assistant", "avatar":"🤖", "content": response})



