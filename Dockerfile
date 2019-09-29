FROM python:3.7


RUN apt update
RUN apt install -y postgresql python-psycopg2 libpq-dev

WORKDIR /ng
COPY netguru_app /ng
COPY requirements.txt /ng/requirements.txt
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD gunicorn movie_database.wsgi:application
