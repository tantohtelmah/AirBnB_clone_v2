#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
=======
"""create a unique FileStorage instance for your application"""
>>>>>>> 1156c05fb75c5fd7b5d100a1c39df07cd3bfb97a
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


# Determine the storage type based on the environment variable
storage_type = os.getenv("HBNB_TYPE_STORAGE", "file")

# Initialize the appropriate storage engine
if storage_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Load data from storage (if needed)
storage.reload()
