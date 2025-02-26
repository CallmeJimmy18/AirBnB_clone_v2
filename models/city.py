#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='cities',
                          cascade='all, delete, delete-orphan')
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
