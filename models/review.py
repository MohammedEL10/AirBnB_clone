#!/usr/bin/python3

"""review Module:
inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class that inherits from BaseModel."""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
