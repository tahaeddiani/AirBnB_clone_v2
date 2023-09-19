#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        vrp = models.storage.all()
        liste = []
        resultat = []
        for i in vrp:
            city = i.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                liste.append(vrp[i])
        for element in liste:
            if (element.state_id == self.id):
                resultat.append(element)
        return (resultat)
