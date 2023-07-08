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
