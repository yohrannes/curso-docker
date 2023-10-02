FROM python:3

RUN apt-get update -y && \
apt-get install -y pip python-dev-is-python3

WORKDIR /app

RUN pip install Flask requests Flask-MySQLdb

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]