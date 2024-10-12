# app/services/user_service.py

"""
Service layer for User operations.

This module contains the business logic for managing users.
It interacts with the `UserModel` from the database and uses
the `User` Pydantic model for data validation.
"""

from typing import Optional
from peewee import DoesNotExist
from config.database import UserModel, RoleModel
from models.user import User


class UserService:
    """Service layer for User operations"""

    @staticmethod
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

        Raises:
            ValueError: If the role with the given ID does not exist.
        """
        try:
            role_instance = RoleModel.get_by_id(role_id)
            user_instance = UserModel.create(
                name=name, email=email, password=password, role=role_instance
            )
            # Using from_orm to convert Peewee model to Pydantic model
            return User.from_orm(user_instance)
        except DoesNotExist as exc:
            raise ValueError(f"Role with id {role_id} not found") from exc

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """
        Retrieve a user by ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[User]: The user instance if found, else None.
        """
        try:
            user_instance = UserModel.get_by_id(user_id)
            # Using from_orm to convert Peewee model to Pydantic model
            return User.from_orm(user_instance)
        except DoesNotExist:
            return None

    @staticmethod
    def update_user(
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        role_id: Optional[int] = None,
    ) -> Optional[User]:
        """
        Update an existing user by ID.

        Args:
            user_id (int): The ID of the user to update.
            name (Optional[str]): The new name of the user.
            email (Optional[str]): The new email of the user.
            password (Optional[str]): The new password of the user.
            role_id (Optional[int]): The new role's ID.

        Returns:
            Optional[User]: The updated user instance if successful, else None.

        Raises:
            ValueError: If the role with the given ID does not exist.
        """
        try:
            user_instance = UserModel.get_by_id(user_id)

            # Update fields only if new values are provided
            if name:
                user_instance.name = name
            if email:
                user_instance.email = email
            if password:
                user_instance.password = password
            if role_id:
                try:
                    role_instance = RoleModel.get_by_id(role_id)
                    user_instance.role = role_instance
                except DoesNotExist as exc:
                    raise ValueError(f"Role with id {role_id} not found") from exc

            user_instance.save()
            return User.from_orm(user_instance)

        except DoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """
        Delete a user by ID.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted, else False.
        """
        try:
            # Check if the user exists before attempting to delete
            user_instance = UserModel.get_by_id(user_id)
            user_instance.delete_instance()
            return True
        except DoesNotExist:
            return False
