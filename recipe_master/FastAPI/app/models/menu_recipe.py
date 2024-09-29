"""
This module contains the MenuRecipe model for representing the relationship 
between menus and recipes.
"""

from pydantic import BaseModel

class MenuRecipe(BaseModel):
    """
    MenuRecipe model representing the association between a menu and a recipe.
    """
    menu_id: int
    recipe_id: int
