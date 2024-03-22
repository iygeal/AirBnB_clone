#!/usr/bin/python3
"""Module that defines the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class represents City"""

    # Public class attributes
    state_id = ""
    name = ""
