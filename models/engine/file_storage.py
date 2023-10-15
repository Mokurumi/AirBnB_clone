#!/usr/bin/python3
"""
This module handles file storage functions
"""


import json
import importlib


class FileStorage:
    """
    This class handles serialization and deserialization of objects
        to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds an object to the internal dictionary.

        Args:
            obj: The object to add.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes and saves the dictionary of objects to a JSON file."""
        data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes and loads objects from the JSON file."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for key, obj_data in data.items():
                class_name, obj_id = key.split('.')
                # Dynamically import the class with the correct module name
                module = importlib.import_module("models." + class_name)
                class_ = getattr(module, class_name)
                new_instance = class_(**obj_data)
                self.__objects[key] = new_instance
        except FileNotFoundError:
            pass
