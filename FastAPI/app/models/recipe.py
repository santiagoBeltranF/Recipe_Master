"""
This module contains the models for Category, Difficulty, and Recipe.
"""

from pydantic import BaseModel

class Category(BaseModel):
    """
    Category model representing a category with an id and a name.
    """
    id: int
    name: str

class Difficulty(BaseModel):
    """
    Difficulty model representing a difficulty level with an id and a name.
    """
    id: int
    name: str

class Recipe(BaseModel):
    """
    Recipe model representing a recipe with an id, name, instruction, preparation_time, 
    difficulty level, category, and user_id.
    """
    id: int
    name: str
    instruction: str
    preparation_time: int
    difficulty: Difficulty
    category: Category
    user_id: int
