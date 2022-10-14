#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class definition for a user

    Attributes:
        email (str): email address
        password (str): passcode
        first_name (str): first name
        last_name (str): last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
