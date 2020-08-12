#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    # TODO add or replace class attributes
    __tablename__ = 'states'
    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship(
        'City',
        backref='state',
        cascade="all, delete"
    )
    # TODO should return all cities in file storage with self.id
    if os.getenv("HBNB_TYPE_STORAGE") != 'db':
        from models import storage
        from models.city import City

        @property
        def cities(self):
            """Cities getter"""
            ret = []
            for key, value in self.all(City).items():
                if value.state_id == self.id:
                    ret.append(value)
            return ret
