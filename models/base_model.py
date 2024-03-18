#!/usr/bin/python3
"""Module that defines the BaseModel class"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """The BaseModel class from which other classes inherit"""

    def __init__(self):
        """BaseModel constructor method"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Visualization method for the BaseModel class"""
        str_rep = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return str_rep

    def save(self):
        """Method to update updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict with all keys/values of dict of obj"""

        # Make a copy of the instance dictionary
        obj_dict = dict(self.__dict__)

        # Iterate through the key-value pairs and format datetime to isoformat
        for key, value in obj_dict.items():
            if key in ('created_at', 'updated_at'):
                obj_dict[key] = value.isoformat()

        # Add the __class__ key with value as class name
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict