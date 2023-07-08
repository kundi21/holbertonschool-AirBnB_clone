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
        """serializes object in json format to a file path"""
        try:
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                for key, value in FileStorage.__objects.items():
                    file.write("{}: {}\n".format(key, value.to_dict()))
                json.dump(FileStorage.__objects, file)
                file.close()
        except TypeError:
            pass

    def reload(self):
        """deserializes object from json file"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass
