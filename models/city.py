#!/usr/bin/python3
"""defines user's City"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class defined

    Attributes:
        name (str): string - empty string
        state_id (str): string - empty string: it will be the State.id
    """

    name = ""
    state_id = ""
