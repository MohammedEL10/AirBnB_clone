#!/usr/bin/python3

"""city Module:
inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """city class that inherits from BaseModel
    with Public class attributes
    """
    state_id: str = ""
    name: str = ""
