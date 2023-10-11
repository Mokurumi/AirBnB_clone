#!/usr/bin/python3
"""
This module handles file storage functions
"""


import json


class FileStorage:
    """
    This class handles serialization and deserialization of objects
        to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.

        Returns:
            dict: A dictionary of all objects in the format
                    {'class_name.id': instance}.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds an object to the internal dictionary.

        Args:
            obj: The object to add.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        serialized_data = {
                key: obj.to_dict() for key, obj in self.__objects.items()
                }
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the file exists).
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    obj = obj_class(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
