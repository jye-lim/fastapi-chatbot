#!/usr/bin/env python

####################
# Required Modules #
####################

# Generic/Built-in


# Libs
import streamlit as st

# Custom
from utils import fetch_response, update_chat_history

##################
# Configurations #
##################

st.set_page_config(
    page_title="Chatbot App",
    page_icon="../static/lamini.ico",
)

# Header
st.title("Chatbot App")
st.subheader("Powered by LaMini-LM!")
st.caption("Ask me anything and get instant responses.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input("Ask me anything!"):
    with st.chat_message("user"):
        st.markdown(prompt)
        update_chat_history("user", prompt)

    # Fetch and display assistant response
    response_text = fetch_response(prompt)
    if response_text:
        with st.chat_message("assistant"):
            st.write(response_text)
            update_chat_history("assistant", response_text)

#############
# Functions #
#############


###########
# Classes #
###########


##########
# Script #
##########


if __name__ == "__main__":
    pass
