#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class definition for a review

    Attributes:
        place_id (str): unique id for the place
        user_id (str): unique id of the user
        text (str): short information
    """
    place_id = ""
    user_id = ""
    text = ""
