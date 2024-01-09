#!/usr/bin/python3
"""
console.py
"""
from models.base_model import BaseModel


class User(BaseModel):
    pass

user1 = BaseModel()
print(user1.id)
print(user1)

user2 = User()
print(user2.id)
print(user2)
