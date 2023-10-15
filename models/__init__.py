#!/usr/bin/python3
"""
This module creates a file storage instance for our project
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
