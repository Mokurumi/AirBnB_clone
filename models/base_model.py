#!/usr/bin/python3
"""
The Base class serves as the foundation for other classes in the project.
It manages the 'id' attribute for objects and ensures unique IDs are assigned.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This is the base class for all model objects in the application.
        It provides common attributes and methods.

    Attributes:
        id (str): A unique identifier for the object.
        created_at: The date and time when the object is created.
        updated_at: The date and time when the object is last updated.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes a new BaseModel instance.
            If keyword arguments are provided,
                it populates the instance attributes with the provided values.
            If no arguments are provided,
                it generates a new ID and timestamps for the instance.

        __str__(self):
            Returns a string representation of the object in the format:
                "[<class name>] (<self.id>) <self.__dict__>".

        save(self):
            Updates the 'updated_at' attribute with the current datetime and
                saves the object to the storage.

        to_dict(self):
            Returns a dictionary representation of the object,
                including class name and timestamps.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Not used in this implementation.
            **kwargs: Keyword arguments for populating object attributes.
                If 'created_at' or 'updated_at' is provided,
                    it converts them to datetime objects.

        If keyword arguments are provided,
            it populates the instance attributes with the provided values.
        If no arguments are provided,
            it generates a new ID and timestamps for the instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # For new instances, add them to the storage
            storage.new(self)  # Add this line

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A formatted string with the class name, id,
                and instance attributes.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
            and saves the object to the storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object,
            including class name and timestamps.

        Returns:
            dict: A dictionary containing all attributes of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
