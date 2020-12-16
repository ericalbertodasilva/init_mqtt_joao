FROM python:3.9.0

WORKDIR /app

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential libffi-dev -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

