#!/usr/bin/python3
"""
Data Base Storage Engine(DBStorage)
"""


from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
import os

from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the DBStorage engine.
        """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db_name}",
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        result = {}
        if cls:
            # Query objects of a specific class
            objects = self.__session.query(cls).all()
        else:
            # Query all types of objects
            # Replace the following class names with your actual model classes
            classes_to_query = [User, State, City, Amenity, Place, Review]
            for class_type in classes_to_query:
                objects = self.__session.query(class_type).all()
                for obj in objects:
                    key = f"{class_type.__name__}.{obj.id}"
                    result[key] = obj
        return result
    
    def new(self, obj):
       self.__session.add(obj)
       
    def save(self):
        try:
            self.__session.commit()
            print("Changes commited successfully")
        except:
            print(f"Error committing: {e}")
            self.__session.rollback
            raise

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload data from the database.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))


    def close(self):
        """
        Close the session.
        """
        self.__session.remove()
