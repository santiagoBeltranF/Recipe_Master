"""
This module contains the SuggestionRecipeIngredient model for representing the association 
between suggestion recipes and ingredients.
"""

from pydantic import BaseModel

class SuggestionRecipeIngredient(BaseModel):
    """
    SuggestionRecipeIngredient model representing the association between a suggestion recipe 
    and an ingredient with suggestion_recipe_id, ingredient_id, and missing status.
    """
    suggestion_recipe_id: int
    ingredient_id: int
    missing: bool
