"""
Module defining the routes for managing users.

This module uses FastAPI to define CRUD routes for users,
allowing the creation, retrieval, updating, and deletion of users via a REST API.
"""

from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService # pylint: disable=import-error
from app.models.user import UserResponse, UserCreate, UserUpdate # pylint: disable=import-error

router = APIRouter()


@router.post("/users/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate) -> UserResponse:
    """
    Create a new user.

    Args:
        user (UserCreate): The user data to create.

    Returns:
        UserResponse: The created user.

    Raises:
        HTTPException: If the role is invalid or the email is already in use.
    """
    try:
        created_user = UserService.create_user(
            name=user.name,
            email=user.email,
            password=user.password,
            role_id=user.role_id,
        )
        return created_user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve)) from ve


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int) -> UserResponse:
    """
    Retrieve user information by ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        UserResponse: The user with the specified ID.

    Raises:
        HTTPException: If the user is not found.
    """
    user = UserService.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate) -> UserResponse:
    """
    Update user information.

    Args:
        user_id (int): The ID of the user to update.
        user (UserUpdate): The new user data.

    Returns:
        UserResponse: The updated user.

    Raises:
        HTTPException: If the user is not found or the role/email is invalid.
    """
    try:
        updated_user = UserService.update_user(
            user_id=user_id,
            name=user.name,
            email=user.email,
            password=user.password,
            role_id=user.role_id,
        )
        if updated_user:
            return updated_user
        raise HTTPException(status_code=404, detail="User not found")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve)) from ve


@router.delete("/users/{user_id}", status_code=200)
def delete_user(user_id: int) -> dict:
    """
    Delete a user by ID.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        dict: Confirmation message if the user was deleted.

    Raises:
        HTTPException: If the user is not found.
    """
    if UserService.delete_user(user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
