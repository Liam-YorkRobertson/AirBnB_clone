#!/usr/bin/python3
"""defines user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class for user names

    atrributes:
        email (str): string - empty string
        password (str): string - empty string
        first_name (str): string - empty string
        last_name (str): string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
