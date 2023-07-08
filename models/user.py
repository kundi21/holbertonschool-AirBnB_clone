#!/usr/bin/python3
"""
    Class User that inherits from BaseModel:
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        Users Class.

        email: string
        password: string
        first_name: string
        last_name: string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
            Constructor.
        """
        super().__init__(*args, **kwargs)
    
    def to_dict(self):
        """Return a dictionary representation of a User."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
