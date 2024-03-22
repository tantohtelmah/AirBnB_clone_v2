#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


# Determine the storage type based on the environment variable
storage_type = os.getenv("HBNB_TYPE_STORAGE", "file")

# Initialize the appropriate storage engine
if storage_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Load data from storage (if needed)
storage.reload()
