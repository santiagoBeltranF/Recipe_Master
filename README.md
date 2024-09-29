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

### ▶️ Running the Application

1. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the application**:

    ```bash
    python main.py
    ```