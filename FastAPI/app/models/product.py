"""
This module contains the Product model for representing product data.
"""

from pydantic import BaseModel

class Product(BaseModel):
    """
    Product model representing a product with an id and a name.
    """
    id: int
    name: str
