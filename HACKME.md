# Dependencies

- Python 3.10
- pipenv
- Docker for running the Postgres database for local development

## Installation

Download python 3.10 from https://www.python.org/downloads/ or use any other packagemanager you are used to.
Download Docker Desktop from https://www.docker.com/products/docker-desktop/

Install the dependencies into a virtual environment:

```
pipenv install
```

## Development

To start development activate the virtual environment by running

```
pipenv shell
```

In order to start the development database run

```
docker compose up
```

Open a new shell, create the database models, and start the development server

```
cd organizer
python manage.py migrate
python manage.py runserver
```

Navigate to http://localhost:8000/home
