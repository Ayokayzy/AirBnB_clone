#!/usr/bin/python3
"""
models/base_model.py
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This class defines all common attributes/methods
    for other classes in this project
    """

    def __init__(self):
        """initializes once an instance is created"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints the string representation of the class"""
        return str("[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.created_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        return {
            **self.__dict__,
            "__class__":  BaseModel.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
