# 🍲 Recipe_Master

¡Bienvenido a **Recipe_Master**! Esta aplicación te ayuda a organizar tus recetas de cocina, planificar menús, generar listas de compras y sugerir recetas basadas en los ingredientes disponibles.

## 🚀 Requisitos previos

1. 🐍 **Python 3.x**
2. 🐳 **Docker**
3. 🛠️ **Docker Compose**

### 🐍 Instalación de Python en Linux

1. Verifica si tienes Python instalado ejecutando:

    ```bash
    python3 --version
    ```

2. Si no está instalado, puedes instalarlo con:

    ```bash
    sudo apt update
    sudo apt install python3 python3-venv python3-pip
    ```

### 🌐 Creación del entorno virtual

1. Navega a la carpeta raíz del proyecto en tu terminal.
2. Crea un entorno virtual ejecutando:

    ```bash
    python3 -m venv venv
    ```

3. **Activar el entorno virtual**:

    ```bash
    source venv/bin/activate
    ```

4. **Desactivar el entorno virtual**:

    ```bash
    deactivate
    ```

### 🐳 Instalación de Docker en Linux

1. Actualiza los paquetes existentes:

    ```bash
    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```

2. Añade la clave GPG de Docker:

    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    ```

3. Añade el repositorio de Docker:

    ```bash
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

4. Instala Docker:

    ```bash
    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io
    ```

5. Verifica la instalación:

    ```bash
    docker --version
    ```

6. Añade tu usuario al grupo Docker:

    ```bash
    sudo usermod -aG docker ${USER}
    ```

### ⚙️ Instalación de Docker Compose en Linux

1. Descarga Docker Compose:

    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

2. Otorga permisos de ejecución:

    ```bash
    sudo chmod +x /usr/local/bin/docker-compose
    ```

3. Verifica la instalación:

    ```bash
    docker-compose --version
    ```

### 🏗️ Ejecución de Docker

1. Para correr los contenedores Docker:

    ```bash
    docker-compose up --build
    ```

2. Para detener los contenedores:

    ```bash
    docker-compose down
    ```

### ▶️ Ejecutar la aplicación

1. **Instalar dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Correr la aplicación**:

    ```bash
    python main.py
    ```

### 👥 Contribuciones