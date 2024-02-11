#!/usr/bin/python3

"""user Module:
inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """user class that inherits from BaseModel.
    this creates the profile for user"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
