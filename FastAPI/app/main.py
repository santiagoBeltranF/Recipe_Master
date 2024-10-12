"""
Main FastAPI application with database connection handling.

This module initializes the FastAPI application and sets up the database
connection management using an asynchronous lifespan function. It also
redirects the root path to the API documentation.
"""

from contextlib import asynccontextmanager
from config.database import database as connection
from routes import role_routes
from routes import user_routes
from fastapi import FastAPI


@asynccontextmanager
# pylint: disable=unused-argument, redefined-outer-name
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for handling database connections.

    Ensures the database connection is established when the application starts
    and closed when the application stops.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Control is passed to the FastAPI application execution.
    """
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


# Crear la instancia de la aplicación FastAPI con el lifespan para gestionar
# la conexión a la base de datos
app = FastAPI(lifespan=lifespan)

app.include_router(role_routes.router)
app.include_router(user_routes.router)
