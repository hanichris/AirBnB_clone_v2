#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class definition for a state.

    Attributes:
        name (str): name of the state.
    """
    name = ""
