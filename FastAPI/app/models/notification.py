"""
This module contains the Notification model and its associated typeNotification model.
"""

from pydantic import BaseModel

class TypeNotification(BaseModel):
    """
    TypeNotification model representing the type of notification with an id, type, and name.
    """
    id: int
    type: str
    name: str

class Notification(BaseModel):
    """
    Notification model representing a notification with an id, user_id, type, and message.
    """
    id: int
    user_id: int
    type: TypeNotification
    message: str
