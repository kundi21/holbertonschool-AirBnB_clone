#!/usr/bin/python3
"""
    Class Amenity that inherits from BaseModel:
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity Class

        name: string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Constructor
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Return dictionary representation of an instance"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "name": self.name
        }
