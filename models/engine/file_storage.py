#!/usr/bin/python3
"""
file storage class, serialize, deserialize to a JSON file
"""


class FileStorage:
    """serializes, deserializes to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """create object"""

    def save(self):
        """save object"""

    def reload(self):
        """reload object"""
