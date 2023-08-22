#!/usr/bin/python3

"""Defines the Place class."""

from models.base_model import BaseModel

class Place(BaseModel):
    """Representation of a place.

    Attributes:
        city_id (str): ID of the city.
        user_id (str): ID of the user.
        name (str): Name of the place.
        description (str): Description of the place.
        num_rooms (int): Number of rooms.
        num_bathrooms (int): Number of bathrooms.
        max_guests (int): Maximum number of guests.
        price_per_night (int): Price per night.
        latitude (float): Latitude coordinate.
        longitude (float): Longitude coordinate.
        amenity_ids (list): List of amenity IDs.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    num_rooms = 0
    num_bathrooms = 0
    max_guests = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

