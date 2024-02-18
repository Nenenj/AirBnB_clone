#!/usr/bin/python3
<<<<<<< HEAD
"""Module base_model

This Module contains a definition for BaseModel Class
"""

import uuid
from datetime import datetime

=======
''' module for BaseModel class '''
from datetime import datetime
import uuid
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
import models


class BaseModel:
<<<<<<< HEAD
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Basemodel

        Args:
            *args.
            **kwargs (dict): Key/value pairs
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
=======
    ''' BaseModel class '''
    def __init__(self, *args, **kwargs):
        '''
        initation of basemodel

        Args:
        *args: arguments passed in
        **kwargs: arguments with key values

        Return:
        None
        '''
        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        Return:
        string represntation fo object
        '''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        ''' updates date for updated_at attribute '''
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        bs_dict = (
            {
                k: (v.isoformat() if isinstance(v, datetime) else v)
                for (k, v) in self.__dict__.items()
            }
        )
        bs_dict["__class__"] = self.__class__.__name__
        return bs_dict

    def __str__(self) -> str:
        """should print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
=======
        ''' returns dictonary with all key values of instance '''
        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = self.created_at.isoformat()
        mydict['updated_at'] = self.updated_at.isoformat()

        return mydict
>>>>>>> e5b90b32db7477fa668f275f10cd07e955883caa
