"""
Models for the User and Role entities.

This module contains the SQLAlchemy models for User and Role,
defining their attributes and relationships.
"""

from sqlalchemy import Column, Integer, String, ForeignKey # pylint: disable=import-error
from sqlalchemy.ext.declarative import declarative_base # pylint: disable=import-error
from sqlalchemy.orm import relationship, sessionmaker # pylint: disable=import-error
from sqlalchemy import create_engine # pylint: disable=import-error
from config.settings import DATABASE # pylint: disable=import-error

Base = declarative_base()

class Role(Base):
    """
    Model representing a role in the system.

    Attributes:
        id (int): Unique identifier for the role.
        name (str): Name of the role.
    """
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)

    users = relationship("User", back_populates="role")


class User(Base):
    """
    Model representing a user in the system.

    Attributes:
        id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): Email of the user.
        hashed_password (str): Hashed password of the user.
        role_id (int): Foreign key referring to the user's role.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")


# Configurar la base de datos
DATABASE_URL = (
    f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@"
    f"{DATABASE['host']}/{DATABASE['name']}"
)
engine = create_engine(DATABASE_URL)

# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
