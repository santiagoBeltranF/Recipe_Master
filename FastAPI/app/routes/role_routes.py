# app/role_routes.py

"""
Module that defines the routes for managing roles.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting roles through a REST API.

Available routes:

- POST /roles/: Creates a new role.
- GET /roles/{role_id}: Retrieves role information by ID.
- PUT /roles/{role_id}: Updates role information.
- DELETE /roles/{role_id}: Deletes a role.

Each route uses the `RoleService` to interact with the
business logic related to roles.
"""

from services.role_service import RoleService
from models.user import Role
from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/roles",
    tags=["roles"],
)


@router.post("/", response_model=Role)
def create_role(name: str) -> Role:
    """
    Create a new role.

    Args:
        name (str): The name of the role.

    Returns:
        Role: The created role instance.
    """
    role = RoleService.create_role(name)
    return role


@router.get("/{role_id}", response_model=Role)
def get_role(role_id: int) -> Role:
    """
    Retrieve role information by ID.

    Args:
        role_id (int): The ID of the role to retrieve.

    Returns:
        Role: The role with the specified ID.

    Raises:
        HTTPException: If the role is not found.
    """
    role = RoleService.get_role_by_id(role_id)
    if role:
        return role
    raise HTTPException(status_code=404, detail="Role not found")


@router.put("/{role_id}", response_model=Role)
def update_role(role_id: int, name: str) -> Role:
    """
    Update role information.

    Args:
        role_id (int): The ID of the role to update.
        name (str): The new name of the role.

    Returns:
        Role: The updated role instance.

    Raises:
        HTTPException: If the role is not found.
    """
    role = RoleService.update_role(role_id, name)
    if role:
        return role
    raise HTTPException(status_code=404, detail="Role not found")


@router.delete("/{role_id}")
def delete_role(role_id: int) -> dict:
    """
    Delete a role by ID.

    Args:
        role_id (int): The ID of the role to delete.

    Returns:
        dict: A confirmation message if the role was deleted.

    Raises:
        HTTPException: If the role is not found.
    """
    if RoleService.delete_role(role_id):
        return {"message": "Role deleted successfully"}
    raise HTTPException(status_code=404, detail="Role not found")
