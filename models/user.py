#!/usr/bin/python3
<<<<<<< HEAD
"""Module base_model

This Module contains a definition for User Class
"""

=======
''' user module '''
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """A class that represents a user.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

=======
    '''
    initation of User that inherits BaseModel class

    Public Class Attributes:
    (string) email: initalized as empty string
    (string) password: initalized as empty string
    (string) first_name: initalized as empty string
    (string) las_name: initalized as empty string
    '''
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
    email = ""
    password = ""
    first_name = ""
    last_name = ""
