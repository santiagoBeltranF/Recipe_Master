"""
This module contains the Ingredient model for representing ingredient data.
"""

from pydantic import BaseModel

class Ingredient(BaseModel):
    """
    Ingredient model representing an ingredient with an id and a name.
    """
    id: int
    name: str
