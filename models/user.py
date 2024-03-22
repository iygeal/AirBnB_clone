#!/usr/bin/python3
"""Module that defines a class User"""

from models.base_model import BaseModel

class User(BaseModel):
    """A class User that represents users"""

    # Public class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""