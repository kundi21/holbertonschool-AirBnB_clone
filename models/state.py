#!/usr/bin/python3
"""
    Class State that inherits from BaseModel:
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        State Class

        name: string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Returns a dictionary representation of a State."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "name": self.name
        }
