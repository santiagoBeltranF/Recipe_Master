"""
This module contains the Menu model for representing menu data.
"""

from pydantic import BaseModel

class Menu(BaseModel):
    """
    Menu model representing a menu with an id, name, date, and user_id.
    """
    id: int
    name: str
    date: str
    user_id: int
