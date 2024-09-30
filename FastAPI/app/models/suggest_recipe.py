"""
This module contains the SuggestRecipe model for representing user suggestions for recipes.
"""

from pydantic import BaseModel

class SuggestRecipe(BaseModel):
    """
    SuggestRecipe model representing a suggestion with an id, user_id, and recipe_id.
    """
    id: int
    user_id: int
    recipe_id: int
