#!/usr/bin/python3
"""
Defines class BaseModel.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Class BaseModel defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()  # updated when initialized
        if kwargs:
            for key, val in kwargs.items():
                """
                convert date and time keys to obj
                """
                tFormat = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, tFormat)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

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
        models.storage.save()

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
