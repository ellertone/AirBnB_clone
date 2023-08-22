#!/usr/bin/python3

"""Defines the Review class."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Representation of a review.

    Attributes:
        place_id (str): ID of the associated place.
        user_id (str): ID of the user who wrote the review.
        text (str): Content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

