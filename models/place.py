#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class definition for a place.

    Attributes:
        name (str): name of the amenity.
        city_id (str): unique id for the city.
        user_id (str): unique id for the user.
        description (str): short description of the place.
        number_rooms (int): number of rooms.
        number_bathrooms (int): number of bathrooms.
        max_guest (int): maximum number of guests.
        price_by_night (int): cost price for the night.
        latitude (float): latitude gps point.
        longitude (float): longitude gps point.
        amenity_ids (list): list of all unique ids of the places.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
