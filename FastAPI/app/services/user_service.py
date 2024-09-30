"""
Service layer for User operations.

This module contains the business logic for managing users.
It interacts with the UserModel and RoleModel from the database
and uses the Pydantic User models for data validation.
"""

from typing import Optional
from app.database import UserModel, RoleModel  # pylint: disable=import-error
from app.models.user import UserResponse  # pylint: disable=import-error
from peewee import DoesNotExist


class UserService:
    """Service layer for User operations."""

    ALLOWED_ROLES = {"ADMINISTRATOR", "MEMBER"}

    @staticmethod
    def create_user(name: str, email: str, password: str, role_id: int) -> UserResponse:
        """
        Create a new user.

        Args:
            name (str): The name of the user.
            email (str): The email address of the user.
            password (str): The password of the user.
            role_id (int): The ID of the role assigned to the user.

        Returns:
            UserResponse: The created user as a Pydantic model.

        Raises:
            ValueError: If the role is invalid or the email already exists.
        """
        try:
            role = RoleModel.get_by_id(role_id)
            if role.name not in UserService.ALLOWED_ROLES:
                raise ValueError(f"Role '{role.name}' is not allowed.")
        except DoesNotExist as exc:
            raise ValueError("Role not found.") from exc

        # Check if the email already exists
        if UserModel.select().where(UserModel.email == email).exists():
            raise ValueError("Email is already in use.")

        # Create the user
        user_instance = UserModel.create(
            name=name, email=email, password=password, role=role
        )

        return UserResponse(
            id=user_instance.id,
            name=user_instance.name,
            email=user_instance.email,
            role={"id": role.id, "name": role.name},
        )

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[UserResponse]:
        """
        Retrieve a user by ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[UserResponse]: The user as a Pydantic model if found, else None.
        """
        try:
            user_instance = UserModel.get_by_id(user_id)
            role = user_instance.role
            return UserResponse(
                id=user_instance.id,
                name=user_instance.name,
                email=user_instance.email,
                role={"id": role.id, "name": role.name},
            )
        except DoesNotExist:
            return None

    @staticmethod
    def update_user(
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        role_id: Optional[int] = None,
    ) -> Optional[UserResponse]:
        """
        Update an existing user by ID.

        Args:
            user_id (int): The ID of the user to update.
            name (Optional[str]): The new name of the user.
            email (Optional[str]): The new email of the user.
            password (Optional[str]): The new password of the user.
            role_id (Optional[int]): The new role ID of the user.

        Returns:
            Optional[UserResponse]: The updated user as a Pydantic model if successful, else None.

        Raises:
            ValueError: If the role is invalid or the email is already in use.
        """
        try:
            user_instance = UserModel.get_by_id(user_id)
        except DoesNotExist:
            return None

        if email and email != user_instance.email:
            # Check if the new email is already in use
            if UserModel.select().where(UserModel.email == email).exists():
                raise ValueError("Email is already in use.")
            user_instance.email = email

        if name:
            user_instance.name = name

        if password:
            user_instance.password = password

        if role_id:
            try:
                role = RoleModel.get_by_id(role_id)
                if role.name not in UserService.ALLOWED_ROLES:
                    raise ValueError(f"Role '{role.name}' is not allowed.")
                user_instance.role = role
            except DoesNotExist as exc:
                raise ValueError("Role not found.") from exc

        user_instance.save()

        return UserResponse(
            id=user_instance.id,
            name=user_instance.name,
            email=user_instance.email,
            role={"id": user_instance.role.id, "name": user_instance.role.name},
        )

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
            user_instance = UserModel.get_by_id(user_id)
            user_instance.delete_instance()
            return True
        except DoesNotExist:
            return False
