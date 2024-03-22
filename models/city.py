#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """City class for database table 'cities'."""

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Establish a relationship with the State class
    state = relationship("State", back_populates="cities")

    # Relationship with Place
    places = relationship('Place', cascade='all, delete-orphan', backref='cities')
    