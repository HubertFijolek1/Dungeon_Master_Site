# Dungeon Master Website

A comprehensive platform for Dungeon Masters to manage campaigns, characters, world-building, and more.

## Features

- Campaign Management
- Character Management
- World Building Tools
- Game Mechanics Integration
- Resource Libraries
- Customization and Personalization

## Setup Instructions

### Prerequisites

- **Docker**: Ensure you have Docker installed on your machine. [Download Docker](https://www.docker.com/get-started)
- **Docker Compose**: Comes with Docker Desktop, but verify installation.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/HubertFijolek1/Dungeon_Master_Site.git
    cd dm_site
    ```

2. **Create a `.env` file:**

    ```bash
    cp .env.example .env
    ```

    Edit `.env` to set your environment variables.

3. **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

    This command builds the Docker images and starts the containers for the web app and PostgreSQL database.

4. **Apply migrations and create a superuser:**

    In another terminal, run:

    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account.

5. **Access the application:**

    - **Website**: [http://localhost:8000](http://localhost:8000) - Displays a simple message indicating the API is running.
    - **Admin Interface**: [http://localhost:8000/admin](http://localhost:8000/admin) - Use the superuser credentials to log in.

## Running the Project Locally Without Docker

If you prefer running the project without Docker, follow these steps:

1. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Rename `.env.example` to `.env` and configure the variables.

4. **Apply migrations and create a superuser:**

    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application:**

    - **Website**: [http://localhost:8000](http://localhost:8000)
    - **Admin Interface**: [http://localhost:8000/admin](http://localhost:8000/admin)

## Additional Commands

- **Stopping the Docker containers:**

    Press `Ctrl+C` in the terminal running `docker-compose up`, then run:

    ```bash
    docker-compose down
    ```

- **Collect static files:**

    ```bash
    docker-compose exec web python manage.py collectstatic
    ```

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **Web Server**: Gunicorn


