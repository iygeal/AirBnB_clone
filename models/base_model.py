#!/usr/bin/python3
"""Module that defines the BaseModel class"""

from datetime import datetime
from uuid import uuid4
from . import storage


class BaseModel:
    """The BaseModel class from which other classes inherit"""

    def __init__(self, *args, **kwargs):
        """BaseModel constructor method"""

        # Check if kwargs is not empty
        if kwargs:
            for key, value in kwargs.items():
                # Exclude __class__
                if key != "__class__":
                    # Convert isoformat strings back to datetime objects
                    if key in ['created_at', 'updated_at']:
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        # Set other keys to their appropriate values
                        setattr(self, key, value)
        else:
            # If kwargs is empty, create new attributes
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Visualization method for the BaseModel class"""
        str_rep = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return str_rep

    def save(self):
        """Method to update updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dict with all keys/values of dict of obj"""

        # Make a copy of the instance dictionary
        obj_dict = self.__dict__.copy() # dict(self.__dict__)

        # Iterate through the key-value pairs and format datetime to isoformat
        for key, value in obj_dict.items():
            if key in ('created_at', 'updated_at'):
                obj_dict[key] = value.isoformat()

        # Add the __class__ key with value as class name
        obj_dict['__class__'] = self.__class__.__name__

        # Return the formatted dictionary
        return obj_dict
