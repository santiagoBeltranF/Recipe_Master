"""
This module contains the Group model for representing group data.
"""

from pydantic import BaseModel

class Group(BaseModel):
    """
    Group model representing a group with an id and a name.
    """
    id: int
    name: str
