# 🍲 Recipe_Master

Welcome to **Recipe_Master**! This application helps you organize your cooking recipes, plan menus, generate shopping lists, and suggest recipes based on available ingredients.

## 🚀 Prerequisites

1. 🐍 **Python 3.12**
2. 🐳 **Docker**
3. 🛠️ **Docker Compose**

### 🐍 Installing Python on Linux

1. Check if you have Python 3.12 installed by running:

    ```bash
    python3 --version
    ```

2. If it's not installed, you can install it from the official Python website or by using a package manager like apt (the availability of Python 3.12 in apt depends on your Linux distribution):

    ```bash
    # Example with apt (may vary depending on the distribution)
    sudo apt update
    sudo apt install python3.12 python3.12-venv python3.12-pip
    ```

    **Note:** Adjust the commands according to your Linux distribution and the way Python 3.12 is provided.

### 🌐 Creating the Virtual Environment

1. Navigate to the project's root folder in your terminal.
2. Create a virtual environment by running (remember to use python3.12):

    ```bash
    python3.12 -m venv venv
    ```

3. **Activating the virtual environment**:

    ```bash
    source venv/bin/activate
    ```

4. **Deactivating the virtual environment**:

    ```bash
    deactivate
    ```

### 🐳 Installing Docker on Linux

1. Update existing packages:

    ```bash
    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```

2. Add Docker's GPG key:

    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    ```

3. Add the Docker repository:

    ```bash
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

4. Install Docker:

    ```bash
    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io
    ```

5. Verify the installation:

    ```bash
    docker --version
    ```

6. Add your user to the Docker group:

    ```bash
    sudo usermod -aG docker ${USER}
    ```

### ⚙️ Installing Docker Compose on Linux

1. Download Docker Compose:

    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

2. Grant execution permissions:

    ```bash
    sudo chmod +x /usr/local/bin/docker-compose
    ```

3. Verify the installation:

    ```bash
    docker-compose --version
    ```

### 🏗️ Running Docker

1. To run the Docker containers:

    ```bash
    docker-compose up --build
    ```

2. To stop the containers:

    ```bash
    docker-compose down
    ```
Here’s the revised README section in English with additional details and emojis to make it more intuitive and attractive:

---

## Database Migrations with Alembic ⚙️

### Commands to Run Migrations from the Terminal 🖥️

You can run migration commands directly from the terminal with the following steps:

1. **Generate the first migration revision** 📜:
   ```bash
   docker-compose exec fastapi alembic revision --autogenerate -m "first_migrations"
   ```

2. **Apply the migration to the database** 🚀:
   ```bash
   docker-compose exec fastapi alembic upgrade head
   ```

### Remove Alembic Directory to Run Migrations on Your Machine 🧹

If you need to set up Alembic on your local machine, you can remove the current Alembic directory and reinitialize it by running:

```bash
alembic init alembic
```

### Configure `env.py` for Migrations 🛠️

Copy this code into your `env.py` file to configure database migrations:

```python
"""
This module configures Alembic to handle database migrations.

It is responsible for establishing the connection to the database and defining
the behavior of migrations, both in 'offline' and 'online' modes.
"""

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from migrations import Base, DATABASE_URL  # pylint: disable=import-error

# This Alembic configuration object provides access to the
# values within the ini file in use.
config = context.config  # pylint: disable=no-member
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Interpret the config file for logging configuration.
# This line essentially configures the loggers.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object here for 'autogenerate' support.
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL and not with an Engine,
    although an Engine is also acceptable here. By skipping the creation
    of the Engine, we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to
    the script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(  # pylint: disable=no-member
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():  # pylint: disable=no-member
        context.run_migrations()  # pylint: disable=no-member

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario, we need to create an Engine and associate a
    connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)  # pylint: disable=no-member

        with context.begin_transaction():  # pylint: disable=no-member
            context.run_migrations()  # pylint: disable=no-member

if context.is_offline_mode():  # pylint: disable=no-member
    run_migrations_offline()
else:
    run_migrations_online()
```

---

This version enhances clarity and makes the steps more engaging with the use of emojis.
