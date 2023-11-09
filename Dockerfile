FROM python:3.8

WORKDIR /app

COPY . /app

RUN  pip3 install -r requirements.txt

EXPOSE 8000

CMD ["bash","-c","python manage.py makemigrations && python manage.py migrate && gunicorn --bind :8000 pproj.wsgi:application"]