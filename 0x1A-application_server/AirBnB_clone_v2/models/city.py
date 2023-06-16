#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),  ForeignKey('states.id'), nullable=False)

        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
