FROM python:3.9.7

WORKDIR /app/codecup/

RUN apt-get update && apt-get install -y curl

COPY requirements.txt /app/codecup
ENV PIP_NO_CACHE_DIR 1
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

COPY . .
