#!/usr/bin/python3

"""state Module:
inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """state class that inherits from BaseModel."""
    name: str = ""
