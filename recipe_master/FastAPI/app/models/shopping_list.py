"""
This module contains the ShoppingList model for representing shopping list data.
"""

from pydantic import BaseModel

class ShoppingList(BaseModel):
    """
    ShoppingList model representing a shopping list with an id and a menu_id.
    """
    id: int
    menu_id: int
