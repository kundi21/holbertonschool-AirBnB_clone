#!/usr/bin/python3
"""Base Model"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base Model Class"""

    def __init__(self):
        """Initialization (generate id and datetime)"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        storage.new(self)

    def update_timestamp(self):
        """Update datetime"""
        self.updated_at = datetime.now()

    def __srt__(self):
        """String representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save method"""
        self.update_timestamp()
        storage.save()

    def to_dict(self):
        """Convert to dictionary"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
