#!/usr/bin/python3
"""
    Class City that inherits from BaseModel:
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        City Class.

        name: string
        state_id: string
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Returns a dictionary representation of a City instance."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "name": self.name,
            "state_id": self.state_id
        }
