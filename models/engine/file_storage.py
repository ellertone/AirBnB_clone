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

    __file_storage = "file.json"
    __objects = {}

    def all(self):
        """returns all objects stored"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new instance of the class with id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the created object to json format"""
        with open(FileStorage.__file_storage, mode="w", encoding="UTF8") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """Loads the objects stored in the json file back into the dictionary if it exists"""
        if os.path.isfile(FileStorage.__file_storage) and os.access(
            FileStorage.__file_storage, os.R_OK
        ):
            with open(FileStorage.__file_storage, mode="r", encoding="UTF8") as file:
                FileStorage.__objects = json.load(file)
