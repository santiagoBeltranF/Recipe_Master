"""
This module contains the Pantry model for representing pantry data.
"""

from pydantic import BaseModel

class Pantry(BaseModel):
    """
    Pantry model representing a pantry with an id and user_id.
    """
    id: int
    user_id: int
