"""
This module contains the ShoppingListIngredient model for representing the relationship 
between shopping lists and ingredients.
"""

from pydantic import BaseModel

class ShoppingListIngredient(BaseModel):
    """
    ShoppingListIngredient model representing the association between a shopping list and 
    an ingredient with shopping_list_id, ingredient_id, quantity, and purchased status.
    """
    shopping_list_id: int
    ingredient_id: int
    quantity: float
    purchased: bool
