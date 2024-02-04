#!/usr/bin/env python

####################
# Required Modules #
####################

# Generic/Built-in
from copy import deepcopy

# Libs
from fastapi import APIRouter

# Custom
from backend.app.chat import get_response

##################
# Configurations #
##################

router = APIRouter()

#############
# Functions #
#############


@router.get("/")
async def hello():
    """
    Test function to check if the API is running.
    """
    return {"hello": "world"}


@router.get("/test")
async def test():
    """
    Test function to check if the chatbot is working.
    """
    test_qn = "Describe Singapore."
    res = get_response(test_qn)
    result = deepcopy(res)
    return result


@router.get("/chatbot")
async def chatbot(question: str):
    """
    Get response from the chatbot.

    Args:
        question (str): The question to be asked.

    Returns:
        str: The response from the chatbot.
    """
    res = get_response(question)
    result = deepcopy(res)
    return result


###########
# Classes #
###########


##########
# Script #
##########


if __name__ == "__main__":
    pass
