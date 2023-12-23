# LATEST IMAGE
FROM python:3.9

USER root

WORKDIR /usr/test

COPY entrypoint.sh .
COPY requirements.txt .
COPY .env .

#RUN chmod +x entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT "entrypoint.sh"