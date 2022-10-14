#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class definition for a city.

    Attributes:
        name (str): name of the city.
        state_id (str): unique id of the state.
    """
    state_id = ""
    name = ""
