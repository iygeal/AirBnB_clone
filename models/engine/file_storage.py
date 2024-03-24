#!/usr/bin/python3
"""A class to store dict representation of an object in a json file"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """ A class that stores objects in a json file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict '__objects'"""

        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the '__objects' dict"""

        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes the obj to json and saves to a file"""

        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        # Convert the dictionary to a JSON string using json.dumps
        json_str = json.dumps(obj_dict)

        # Open the file in write mode with UTF-8 encoding
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            # Write the JSON string to the file
            f.write(json_str)

    def reload(self):
        """Deserializes a json file"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as jf:
                dict_obj = json.loads(jf.read())
                for key, value in dict_obj.items():
                    class_name = key.split(".")[0]
                    obj = globals()[class_name](**dict_obj[key])
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
