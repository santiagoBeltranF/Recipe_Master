"""
This module contains the RecipeIngredient model for representing the association 
between recipes and ingredients.
"""

from pydantic import BaseModel

class RecipeIngredient(BaseModel):
    """
    RecipeIngredient model representing the association between a recipe and an ingredient 
    with recipe_id, ingredient_id, quantity, and unit.
    """
    recipe_id: int
    ingredient_id: int
    quantity: int
    unit: float
