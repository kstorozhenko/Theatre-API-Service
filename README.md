# Theatre API Service

Theatre API Service is a web service built with Django and Django REST Framework. It provides an API for managing and retrieving information about theatre plays, performances, and reservations.


## Project Structure

The project is organized into several apps, each serving a different part of the API:

- `theatre`: Contains models, views, and serializers for managing theatre-related data such as genres, actors, theatre halls, plays, performances, and tickets.
- `user`: Handles user registration and authentication.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kstorozhenko/Theatre-API-Service
    ```
2. Navigate to the project directory:
    ```bash
    cd theatre-api-service
    ```
3. Build the Docker images:
    ```bash
    docker-compose build
    ```
4. Run the Docker containers:
    ```bash
    docker-compose up
    ```

The API should now be accessible at `http://localhost:8001/`.

## API Endpoints

The API includes the following endpoints:

- `/api/theatre/genres/`
- `/api/theatre/actors/`
- `/api/theatre/theatre_halls/`
- `/api/theatre/plays/`
- `/api/theatre/performances/`
- `/api/theatre/reservations/`
- `/api/user/register/`
- `/api/user/token/`
- `/api/user/token/refresh/`
- `/api/user/token/verify/`
- `/api/user/me/`

## Running the Tests

To run the tests, use the following command:

```bash
docker-compose run app sh -c "python manage.py test && flake8"
