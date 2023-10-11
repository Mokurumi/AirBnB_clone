#!/usr/bin/python3
"""
The Base class serves as the foundation for other classes in the project.
It manages the 'id' attribute for objects and ensures unique IDs are assigned.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    This is a base class that defines common attributes
        and methods for other classes.
    """

    def _init_(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Unused.
            **kwargs: A dictionary containing attribute names and their corresponding values.

        If kwargs is not empty:
            - Each key in kwargs is treated as an attribute name.
            - Each value in kwargs is the value of the corresponding attribute.
            - 'created_at' and 'updated_at' attributes are converted from ISO-formatted strings to datetime objects.
        Otherwise:
            - Generates a unique ID and sets the 'created_at' timestamp to the current datetime.

        Example:
            instance_dict = {
                '_class_': 'MyClass',
                'id': 'some_id',
                'created_at': '2023-10-11T12:34:56.789012',
                'my_attribute': 'some_value'
            }
            my_instance = MyClass(**instance_dict)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '_class_':
                    if key in ['created_at', 'updated_at']:
                        # Convert ISO-formatted string to datetime object
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def _str_(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string in the format
                '[<class name>] (<self.id>) <self._dict_>'.
        """
        return "[{}] ({}) {}".format(
                self._class.name, self.id, self.dict_
                )

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing all attributes of the instance, including class name,
                  'created_at', and 'updated_at' in ISO format.
        """
        data = self._dict_.copy()
        data['_class'] = self.class.name_
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
