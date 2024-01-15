#!/usr/bin/python3
"""
models/city.py
"""
from models.base_model import BaseModel


class City(BaseModel):
    """a class City that inherits from BaseModel"""
    # public class attributes
    state_id = ""
    name = ""
