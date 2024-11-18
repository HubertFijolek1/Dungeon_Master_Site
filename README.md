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
    git clone https://github.com/yourusername/dm_site.git
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

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **Web Server**: Gunicorn

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

[MIT License](LICENSE)
