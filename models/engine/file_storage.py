#!/usr/bin/env python3
"""File storage module
Controls the storage of objects created to local storage in json format
"""
import json
import models
import os


class FileStorage:
    """
    Controls the storage process of created objects to json
    """

    __file_path = "../../file.json"
    __objects = {}

    def all(self):
        """returns all objects stored"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new instance of the class with id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objdict = json.load(file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(file.jsoncls_name)(**o))
        except FileNotFoundError:
            return
