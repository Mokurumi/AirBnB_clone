#!/usr/bin/python3
"""
This module describe the user class that inherits from base
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Public class attributes:
    - email: string - empty string
    - password: string - empty string
    - first_name: string - empty string
    - last_name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.

        Args:
        *args: Not used in this implementation.
        **kwargs: Keyword arguments for populating object attributes.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
