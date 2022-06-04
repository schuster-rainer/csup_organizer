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

Create a `.env` file for configuring the application.

```sh
cat <<EOT >> .env
SECRET_KEY=$(openssl rand -base64 64)
DB_NAME=csup
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=localhost
DJANGO_SETTINGS_MODULE=organizer.settings
EOT
```

The secret key is a random string. If you don't have openssl install you can generate a base64 string at https://generate.plus/en/base64

```sh
openssl rand -base64 64
```

To start development activate the virtual environment by running

```sh
pipenv shell
```

In order to start the development database run

```sh
docker compose up
```

Open a new shell, create the database models, and start the development server

```sh
cd organizer
python manage.py migrate
python manage.py runserver
```

Navigate to http://127.0.0.1:8000/home to view and test the csup app.

### Datamodels

After making changes to a data model you have to update the database by runnning

```sh
python manage.py makemigrations
python manage.py migrate
```

### Adding new packages

We use _pipenv_ for managing packages. If you want to read more about how to use pipenv head over to the [documentation](https://pipenv.pypa.io/en/latest/)
