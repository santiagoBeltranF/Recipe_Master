"""
This module establishes a connection to a MySQL database 
using Peewee ORM and environment variables.
"""

from dotenv import load_dotenv
from .settings import DATABASE
from peewee import (
MySQLDatabase, Model, AutoField, CharField, ForeignKeyField,
DateField, TextField, IntegerField, FloatField, BooleanField
)

# Load environment variables from the .env file
load_dotenv()

# Create a MySQL database instance using environment variables
database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)

# pylint: disable=too-few-public-methods
class RoleModel(Model):
    """Represents a role with attributes such as name."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)

    class Meta:
        """Meta information for the RoleModel."""
        database = database
        table_name = "roles"

# pylint: disable=too-few-public-methods
class UserModel(Model):
    """Represents a user with attributes such as name, email, password, and role."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    password = CharField(max_length=100)
    role = ForeignKeyField(RoleModel, backref='users', on_delete='CASCADE')

    class Meta:
        """Meta information for the UserModel."""
        database = database
        table_name = "users"
