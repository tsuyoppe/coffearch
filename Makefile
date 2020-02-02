makemigrations:
    docker-compose run --rm django python3 manage.py makemigrations

migrate:
    docker-compose run --rm django python3 manage.py migrate

createsuperuser:
    docker-compose run --rm django python3 manage.py createsuperuser