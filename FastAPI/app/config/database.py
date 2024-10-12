"""
This module establishes a connection to a MySQL database 
using Peewee ORM and environment variables.
"""

from dotenv import load_dotenv
from config.settings import DATABASE
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
        database = DATABASE
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
        database = DATABASE
        table_name = "users"

# pylint: disable=too-few-public-methods
class CategoryModel(Model):
    """Represents a category with attributes such as name."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)

    class Meta:
        """Meta information for the CategoryModel."""
        database = DATABASE
        table_name = "categories"

# pylint: disable=too-few-public-methods
class DifficultyModel(Model):
    """Represents a difficulty level with attributes such as name."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)

    class Meta:
        """Meta information for the DifficultyModel."""
        database = DATABASE
        table_name = "difficulties"

# pylint: disable=too-few-public-methods
class RecipeModel(Model):
    """Represents a recipe with attributes such as name, instruction, preparation_time, difficulty, 
    category, and user."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    instruction = TextField()
    preparation_time = IntegerField()
    difficulty = ForeignKeyField(DifficultyModel, backref='recipes', on_delete='CASCADE')
    category = ForeignKeyField(CategoryModel, backref='recipes', on_delete='CASCADE')
    user = ForeignKeyField(UserModel, backref='recipes', on_delete='CASCADE')

    class Meta:
        """Meta information for the RecipeModel."""
        database = DATABASE
        table_name = "recipes"

# pylint: disable=too-few-public-methods
class GroupModel(Model):
    """Represents a group with attributes such as name."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)

    class Meta:
        """Meta information for the GroupModel."""
        database = DATABASE
        table_name = "groups"

# pylint: disable=too-few-public-methods
class IngredientModel(Model):
    """Represents an ingredient with attributes such as name."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)

    class Meta:
        """Meta information for the IngredientModel."""
        database = DATABASE
        table_name = "ingredients"

# pylint: disable=too-few-public-methods
class MenuModel(Model):
    """Represents a menu with attributes such as name, date, and user."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    date = DateField()  # Consider using DateField for proper date handling
    user_id = ForeignKeyField(UserModel, backref='menus', on_delete='CASCADE')

    class Meta:
        """Meta information for the MenuModel."""
        database = DATABASE
        table_name = "menus"

# pylint: disable=too-few-public-methods
class MenuRecipeModel(Model):
    """Represents the association between a menu and a recipe."""

    menu_id = ForeignKeyField(MenuModel, backref='menu_recipes', on_delete='CASCADE')
    recipe_id = ForeignKeyField(RecipeModel, backref='menu_recipes', on_delete='CASCADE')

    class Meta:
        """Meta information for the MenuRecipeModel."""
        database = DATABASE
        table_name = "menu_recipes"

# pylint: disable=too-few-public-methods
class TypeNotificationModel(Model):
    """Represents the type of notification with attributes such as type and name."""

    id = AutoField(primary_key=True)
    type = CharField(max_length=50)  # Puedes ajustar el tamaño según sea necesario
    name = CharField(max_length=100)

    class Meta:
        """Meta information for the TypeNotificationModel."""
        database = DATABASE
        table_name = "type_notifications"

# pylint: disable=too-few-public-methods
class NotificationModel(Model):
    """Represents a notification with attributes such as user, type, and message."""

    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='notifications', on_delete='CASCADE')
    type = ForeignKeyField(TypeNotificationModel, backref='notifications', on_delete='CASCADE')
    message = TextField()

    class Meta:
        """Meta information for the NotificationModel."""
        database = DATABASE
        table_name = "notifications"

# pylint: disable=too-few-public-methods
class PantryModel(Model):
    """Represents a pantry with attributes such as user."""

    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='pantries', on_delete='CASCADE')

    class Meta:
        """Meta information for the PantryModel."""
        database = DATABASE
        table_name = "pantries"

# pylint: disable=too-few-public-methods
class ProductModel(Model):
    """Represents a product with attributes such as name."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)

    class Meta:
        """Meta information for the ProductModel."""
        database = DATABASE
        table_name = "products"

# pylint: disable=too-few-public-methods
class PantryProductModel(Model):
    """Represents a product in a pantry with attributes such as pantry, product,
     quantity, and unit."""

    pantry_id = ForeignKeyField(PantryModel, backref='pantry_products', on_delete='CASCADE')
    product_id = ForeignKeyField(ProductModel, backref='pantry_products', on_delete='CASCADE')
    quantity = FloatField()  # Para manejar cantidades decimales
    unit = IntegerField()     # Puedes definir un modelo separado para unidades si es necesario

    class Meta:
        """Meta information for the PantryProductModel."""
        database = DATABASE
        table_name = "pantry_products"

# pylint: disable=too-few-public-methods
class RecipeIngredientModel(Model):
    """Represents the association between a recipe and an ingredient with attributes such as
     recipe, ingredient, quantity, and unit."""

    recipe_id = ForeignKeyField(RecipeModel, backref='recipe_ingredients', on_delete='CASCADE')
    ingredient_id = ForeignKeyField(IngredientModel, backref='recipe_ingredients',
    on_delete='CASCADE')
    quantity = IntegerField()  # Para manejar la cantidad del ingrediente
    unit = FloatField()        # Puedes definir un modelo separado para unidades si es necesario

    class Meta:
        """Meta information for the RecipeIngredientModel."""
        database = DATABASE
        table_name = "recipe_ingredients"

# pylint: disable=too-few-public-methods
class ShoppingListModel(Model):
    """Represents a shopping list with attributes such as menu."""

    id = AutoField(primary_key=True)
    menu_id = ForeignKeyField(MenuModel, backref='shopping_lists', on_delete='CASCADE')

    class Meta:
        """Meta information for the ShoppingListModel."""
        database = DATABASE
        table_name = "shopping_lists"

# pylint: disable=too-few-public-methods
class ShoppingListIngredientModel(Model):
    """Represents the association between a shopping list and an ingredient with 
    attributes such as shopping list, ingredient, quantity, and purchased status."""

    shopping_list_id = ForeignKeyField(ShoppingListModel,
    backref='shopping_list_ingredients', on_delete='CASCADE')
    ingredient_id = ForeignKeyField(IngredientModel, backref='shopping_list_ingredients',
    on_delete='CASCADE')
    quantity = FloatField()  # Para manejar cantidades decimales
    purchased = BooleanField(default=False)  # Estado de compra del ingrediente

    class Meta:
        """Meta information for the ShoppingListIngredientModel."""
        database = DATABASE
        table_name = "shopping_list_ingredients"

# pylint: disable=too-few-public-methods
class SuggestRecipeModel(Model):
    """Represents a suggestion with attributes such as user and recipe."""

    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='suggested_recipes', on_delete='CASCADE')
    recipe_id = ForeignKeyField(RecipeModel, backref='suggested_recipes', on_delete='CASCADE')

    class Meta:
        """Meta information for the SuggestRecipeModel."""
        database = DATABASE
        table_name = "suggest_recipes"

# pylint: disable=too-few-public-methods
class SuggestionRecipeIngredientModel(Model):
    """Represents the association between a suggestion recipe and 
    an ingredient with attributes such as suggestion recipe, ingredient, and missing status."""

    suggestion_recipe_id = ForeignKeyField(SuggestRecipeModel,
    backref='suggestion_recipe_ingredients',on_delete='CASCADE')
    ingredient_id = ForeignKeyField(IngredientModel,
    backref='suggestion_recipe_ingredients', on_delete='CASCADE')
    missing = BooleanField(default=False)  # Indica si el ingrediente está faltando

    class Meta:
        """Meta information for the SuggestionRecipeIngredientModel."""
        database = DATABASE
        table_name = "suggestion_recipe_ingredients"
