#!/usr/bin/python3
"""
    Class Review that inherits from BaseModel:
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review Class

        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
            Constructor
        """
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Returns dictionary representation of Review"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "place_id": self.place_id,
            "user_id": self.user_id,
            "text": self.text
        }
