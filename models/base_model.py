#!/usr/bin/python3
"""
Defines class BaseModel.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Class BaseModel defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()  # updated when initialized

    def __str__(self):
        """
        Returns string representation of instance.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates updated_at.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary representation of instance.
        """
        return {
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
