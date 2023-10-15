#!/usr/bin/python3
"""
This module describe the user class that inherits from base
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
