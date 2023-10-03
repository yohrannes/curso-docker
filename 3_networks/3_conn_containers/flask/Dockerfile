FROM python:3

RUN apt-get update -y && \
apt-get install -y python3-pip python3-dev

WORKDIR /app

RUN pip install Flask==2.3.3 requests flask_mysqldb

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]