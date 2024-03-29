#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models import storage_type
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship('City', backref='state')
    else:
        name = ''

        @property
        def cities(self):
            """returns the list of City instances with
            state_id == current State.id
            """
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
