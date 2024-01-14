#!/usr/bin/python3
"""
models/user.py
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines User for the applications that inherits from BaseModel"""
    #public class attributes
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __init__(self, email="", password="", first_name="", last_name=""):
        """Defines variables for the class when an inistance in created"""
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
