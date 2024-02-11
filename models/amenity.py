#!/usr/bin/python3

"""amenity Module:
inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name: str = ""
