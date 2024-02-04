#!/usr/bin/env python

####################
# Required Modules #
####################

# Generic/Built-in


# Libs
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Custom
from app.model import initialise_model, initialise_pipeline

##################
# Configurations #
##################

# Initialise model and pipeline
tokenizer, base_model = initialise_model()
llm = initialise_pipeline()

# Define the prompt template
template = """{text}"""
prompt = PromptTemplate(template=template, input_variables=["text"])
chat = LLMChain(prompt=prompt, llm=llm)

#############
# Functions #
#############


def get_response(question: str) -> str:
    """
    Get response from the chatbot.

    Args:
        question (str): The question to be asked.

    Returns:
        str: The response from the chatbot.
    """
    response = chat.invoke(question)
    return response


###########
# Classes #
###########


##########
# Script #
##########


if __name__ == "__main__":
    pass
