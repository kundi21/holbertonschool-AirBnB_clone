#!/usr/bin/python3
"""
file storage class, serialize, deserialize to a JSON file
"""
import json


class FileStorage:
    """serializes, deserializes to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """create object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save object in json format to a file"""
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file) 

    def reload(self):
        """reload object"""
