#!/usr/bin/python3
"""A class to store dict representation of an object in a json file"""
import json
from models.base_model import BaseModel


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

		json_str = json.dumps(obj_dict)
		with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
			f.write(json_str)

	def reload(self):
		"""Deserializes a json file"""

		try:
			with open(FileStorage.__file_path, 'r', encoding='utf-8') as jf:
				FileStorage.__objects = json.loads(jf.read())
		except FileNotFoundError:
			pass
