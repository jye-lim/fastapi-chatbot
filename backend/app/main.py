#!/usr/bin/env python

####################
# Required Modules #
####################

# Generic/Built-in


# Libs
from fastapi import FastAPI

# Custom
from app.routes import router

##################
# Configurations #
##################

# Define FastAPI app
app = FastAPI(
    title="API for LaMini chatbot",
    description="FastAPI backend for LaMini chatbot",
    version="0.1.0",
)

# Include the router
app.include_router(router)

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
