# app/user_routes.py

"""
Module that defines the routes for managing users.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting users through a REST API.

Available routes:

- POST /users/: Creates a new user.
- GET /users/{user_id}: Retrieves user information by ID.
- PUT /users/{user_id}: Updates user information.
- DELETE /users/{user_id}: Deletes a user.

Each route uses the `UserService` to interact with the
business logic related to users.
"""

from services.user_service import UserService
from models.user import User
from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=User)
def create_user(name: str, email: str, password: str, role_id: int) -> User:
    """
    Create a new user.

    Args:
        name (str): The name of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        role_id (int): The ID of the assigned role.

    Returns:
        User: The created user instance.
    """
    user = UserService.create_user(name, email, password, role_id)
    return user


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    """
    Retrieve user information by ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        User: The user with the specified ID.

    Raises:
        HTTPException: If the user is not found.
    """
    user = UserService.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: int, name: str = None, email: str = None, password: str = None, role_id: int = None
) -> User:
    """
    Update user information.

    Args:
        user_id (int): The ID of the user to update.
        name (str, optional): The new name of the user.
        email (str, optional): The new email of the user.
        password (str, optional): The new password of the user.
        role_id (int, optional): The new role's ID.

    Returns:
        User: The updated user instance.

    Raises:
        HTTPException: If the user is not found.
    """
    user = UserService.update_user(user_id, name, email, password, role_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{user_id}")
def delete_user(user_id: int) -> dict:
    """
    Delete a user by ID.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        dict: A confirmation message if the user was deleted.

    Raises:
        HTTPException: If the user is not found.
    """
    if UserService.delete_user(user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
