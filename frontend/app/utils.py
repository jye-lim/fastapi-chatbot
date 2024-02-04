#!/usr/bin/env python

####################
# Required Modules #
####################

# Generic/Built-in
import os
import requests

# Libs
import streamlit as st

# Custom


##################
# Configurations #
##################

# Fetch the API URL from the environment variable
API_URL = os.getenv("API_URL")

#############
# Functions #
#############


def fetch_response(question: str) -> str:
    """
    Fetch response from the chatbot API.

    Args:
        question (str): The question to be asked.

    Returns:
        str: The response from the chatbot.
    """
    try:
        response = requests.get(f"{API_URL}?question={question}")
        response.raise_for_status()
        return response.json().get("text", "No text found")
    except requests.RequestException as e:
        st.error(f"Failed to retrieve data from the API: {e}")
        return None


def update_chat_history(role: str, content: str) -> None:
    """
    Append a message to the session state chat history.

    Args:
        str: The role of the message sender. Either "user" or "assistant".
        str: The content of the message.
    """
    st.session_state.messages.append({"role": role, "content": content})


###########
# Classes #
###########


##########
# Script #
##########


if __name__ == "__main__":
    pass
