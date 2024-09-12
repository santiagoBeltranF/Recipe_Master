"""
This module contains the Role and User models for representing user roles and user data.
"""

from pydantic import BaseModel

class Role(BaseModel):
    """
    Role model representing a user role with an id and a name.
    """
    id: int
    name: str

class User(BaseModel):
    """
    User model representing a user with an id, name, email, password, and role.
    """
    id: int
    name: str
    email: str
    password: str
    role: Role
