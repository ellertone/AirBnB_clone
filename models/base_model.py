#!/usr/bin/env python3
"""The base module for the AirBnB console
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Basic methods and variables for all the classes to inherit
    """

    def __init__(self, *args, **kwargs):
        """Inititializing a new base Model
        Arguments
         *args - any used
         **kwargs - dictionaries used
        """
        self.id = self.uuid4(10)
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        format_time = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for k, v in kwargs.items:
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strftime(format_time)

    def save(self):
        """Update time to the current"""
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """Return a dictionary of the Basemodel Class"""

    def __str__(self):
        """Print out the string representation of the class"""
        cls_name = self.__class__.__name__
        return f"[ {cls_name}] ({self.id}) {self.__dict__}"
