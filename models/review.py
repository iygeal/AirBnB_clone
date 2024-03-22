#!/usr/bin/python3
"""Module that defines the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Reviews"""

    # Public class attributes
    place_id = ""
    user_id = ""
    text = ""
