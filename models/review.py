#!/usr/bin/python3
"""
models/review.py
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """a class Review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
