"""
Este módulo carga la configuración de entorno para la aplicación.

Utiliza `dotenv` para cargar las variables de entorno desde un archivo `.env`.
Define la configuración de la base de datos basada en el entorno de la aplicación.

Variables:
    ENV (str): Define el entorno de la aplicación. Por defecto, se asume 'dev' si no se especifica.
    DATABASE (dict): Diccionario con la configuración de la base de datos.
        - name: Nombre de la base de datos.
        - engine: Motor de la base de datos utilizado.
        - user: Usuario para la conexión a la base de datos.
        - password: Contraseña para la conexión a la base de datos.
        - host: Dirección del host de la base de datos.
        - port: Puerto utilizado para la conexión a la base de datos.
"""

import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv(
    "ENV", "dev"
)  # 'dev' será el valor por defecto si no se establece 'ENV'

if ENV == "production":
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),
        "engine": "peewee.MySQLDatabase",  # MySQL como motor de base de datos
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "host": os.getenv("MYSQL_HOST"),
        "port": int(os.getenv("MYSQL_PORT")),
    }
else:
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),
        "engine": "peewee.MySQLDatabase",  # MySQL como motor de base de datos
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "host": os.getenv("MYSQL_HOST"),
        "port": int(os.getenv("MYSQL_PORT")),
    }
