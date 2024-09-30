"""
This module contains the PantryProduct model for representing pantry product data.
"""

from pydantic import BaseModel

class PantryProduct(BaseModel):
    """
    PantryProduct model representing a product in a pantry with a pantry_id, product_id, 
    quantity, and unit.
    """
    pantry_id: int
    product_id: int
    quantity: float
    unit: int
