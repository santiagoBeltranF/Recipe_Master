"""
Initialization module for the routes package.

This module imports and makes available the routers for handling
user and role routes.

Modules:
    - user_routes: Contains the router for user-related routes.
    - role_routes: Contains the router for role-related routes.

Available Routers:
    - users_router: Router for user-related routes.
    - roles_router: Router for role-related routes.
"""

from routes.user_routes import router as users_router
from routes.role_routes import router as roles_router

# Define what routers will be available for public import
__all__ = [
    "users_router",
    "roles_router",
]
