#!/usr/bin/env python

####################
# Required Modules #
####################

# Generic/Built-in


# Libs
import torch
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Custom
from config import MODEL_PATH

##################
# Configurations #
##################


#############
# Functions #
#############


def initialise_model() -> tuple:
    """
    Initialise the model and tokenizer.

    Returns:
        tokenizer: Tokenizer object
        base_model: Model object
    """
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    base_model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_PATH, device_map="auto", torch_dtype=torch.float32
    )
    return tokenizer, base_model


def initialise_pipeline() -> HuggingFacePipeline:
    """
    Initialise the pipeline.

    Returns:
        llm: HuggingFacePipeline object
    """
    llm = HuggingFacePipeline.from_model_id(
        model_id=MODEL_PATH, task="text2text-generation"
    )
    return llm


###########
# Classes #
###########


##########
# Script #
##########


if __name__ == "__main__":
    pass
