#!/usr/bin/python3
<<<<<<< HEAD
"""Module base_model

This Module contains a definition for Amenity Class
"""

=======
""" module for Review class """
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """A class that represents a review

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

=======
    """
    initiation of Review that inherits from BaseModel class

    Public Class Attributes:
       (string) place_id: initalized as empty string
       (string) user_id: initalized as empty string
       (string) text: initalized as empty string
    """
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
    place_id = ""
    user_id = ""
    text = ""
