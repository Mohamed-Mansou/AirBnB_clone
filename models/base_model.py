#!/usr/bin/python3

""" Base model class which is the parent class"""

import models
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self,id,*args, **kwargs):
        if kwargs:
            pass
        self.id=id.uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        """ the string representation"""
        return "[{}],({}),{}".format(self.__class__.__name__,self.id,self.__dict__)
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        """ import storage variable"""
        models.storage.save()
        
    def to_dict(self):
        """  returns a dictionary containing all keys/values of __dict__ of the instance """
        this_my_dict = self.__dict__.copy()
        this_my_dict["created_at"] = self.created_at.isoformat()
        this_my_dict["updated_at"] = self.updated_at.isoformat()
        this_my_dict["__class__"] = self.__class__.__name__
        return this_my_dict