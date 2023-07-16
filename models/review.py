#!/usr/bin/python3
"""defines user's Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class defined

    Attributes:
        place_id (str): string - empty string: it will be the Place.id
        user_id (str): string - empty string: it will be the User.id
        text (str): string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
