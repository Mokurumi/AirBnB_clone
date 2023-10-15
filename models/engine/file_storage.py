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

    # Include the new classes in the list of allowed classes
    allowed_classes = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review',
        # Add other classes here if necessary
    ]

    def all(self, cls=None):
        """
        Returns a dictionary of objects, optionally filtered by class.

        Args:
            cls (str, optional): The class name to filter by.
                                    If None, returns all objects.

        Returns:
            dict: A dictionary of objects, filtered by class if cls is provided.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {
                    key: value for key,
                    value in self.__objects.items() if cls == key.split('.')[0]
                    }
            return filtered_objects

    def new(self, obj):
        """
        Adds an object to the internal dictionary.

        Args:
            obj: The object to add.
        """
        key = "{}.{}".format(obj._class.name_, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes _objects to the JSON file (_file_path).
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
