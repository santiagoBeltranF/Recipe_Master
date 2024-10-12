# app/services/role_service.py

"""
Service layer for Role operations.

This module contains the business logic for managing roles.
It interacts with the `RoleModel` from the database and uses
the `Role` Pydantic model for data validation.
"""

from typing import Optional
from peewee import DoesNotExist
from config.database import RoleModel
from models.user import Role


class RoleService:
    """Service layer for Role operations"""

    @staticmethod
    def create_role(name: str) -> Role:
        """
        Create a new role.

        Args:
            name (str): The name of the role.

        Returns:
            Role: The created role instance.
        """
        role_instance = RoleModel.create(name=name)
        # Using from_orm to convert Peewee model to Pydantic model
        return Role.from_orm(role_instance)

    @staticmethod
    def get_role_by_id(role_id: int) -> Optional[Role]:
        """
        Retrieve a role by ID.

        Args:
            role_id (int): The ID of the role to retrieve.

        Returns:
            Optional[Role]: The role instance if found, else None.
        """
        try:
            role_instance = RoleModel.get_by_id(role_id)
            # Using from_orm to convert Peewee model to Pydantic model
            return Role.from_orm(role_instance)
        except DoesNotExist:
            return None

    @staticmethod
    def update_role(role_id: int, name: str) -> Optional[Role]:
        """
        Update an existing role by ID.

        Args:
            role_id (int): The ID of the role to update.
            name (str): The new name of the role.

        Returns:
            Optional[Role]: The updated role instance if successful, else None.
        """
        try:
            role_instance = RoleModel.get_by_id(role_id)
            role_instance.name = name
            role_instance.save()
            return Role.from_orm(role_instance)
        except DoesNotExist:
            return None

    @staticmethod
    def delete_role(role_id: int) -> bool:
        """
        Delete a role by ID.

        Args:
            role_id (int): The ID of the role to delete.

        Returns:
            bool: True if the role was deleted, else False.
        """
        try:
            # Check if the role exists before attempting to delete
            role_instance = RoleModel.get_by_id(role_id)
            role_instance.delete_instance()
            return True
        except DoesNotExist:
            return False
