"""
This module contains Pydantic models for representing user data and roles.
"""

from typing import Optional

from pydantic import BaseModel, EmailStr


class Role(BaseModel):
    """
    Role model representing a user role with an ID and a name.
    """

    id: int
    name: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration for the Role model.
        Sets orm_mode to True to enable compatibility with SQLAlchemy models.
        """

        orm_mode = True


class UserBase(BaseModel):
    """
    Base User model with shared attributes.
    """

    id: int
    name: str
    email: EmailStr
    role: Role

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration for the Role model.
        Sets orm_mode to True to enable compatibility with SQLAlchemy models.
        """

        orm_mode = True


class UserCreate(BaseModel):
    """
    User model for creating a new user.
    """

    name: str
    email: EmailStr
    password: str
    role_id: int


class UserUpdate(BaseModel):
    """
    User model for updating existing user details.
    """

    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role_id: Optional[int] = None


class UserResponse(UserBase):
    """
    User model for API responses, excluding sensitive information like password.
    """
