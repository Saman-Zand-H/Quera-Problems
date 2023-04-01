FROM python:3.10.4-slim

WORKDIR /app/codecup/

RUN apt update && apt install -y curl

COPY requirements.txt /app/codecup

RUN pip --timeout=20000000 install -r requirements.txt
RUN pip --timeout=20000000 install psycopg2-binary

COPY . .
