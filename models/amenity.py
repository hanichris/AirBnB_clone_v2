#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class definition for an amenity.

    Attributes:
        name (str): name of the amenity.
    """
    name = ""
