#!/usr/bin/python3
"""
models/user.py
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines User for the applications that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
