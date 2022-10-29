#!/usr/bin/python3
"""
class user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherited class User from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """the init constructor"""
        super().__init__(**kwargs)
