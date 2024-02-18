#!/usr/bin/python3
<<<<<<< HEAD
"""Module base_model

This Module contains a definition for City Class
"""

=======
""" module for City class """
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
from models.base_model import BaseModel


class City(BaseModel):
<<<<<<< HEAD
    """A class that represents a city

    Attributes:
        name (str): name of the city
        state_id (str): the state id
    """

=======
    """
    initiation of City that inherits from BaseModel class

    Public Class Attributes:
       (string) state_id: initialized as empty string
       (string) name: initialized as empty string
    """
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
    state_id = ""
    name = ""
