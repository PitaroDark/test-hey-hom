# LATEST IMAGE
FROM python:3.9

USER root

WORKDIR /usr/test

COPY entrypoint.sh /usr/test/entrypoint.sh
COPY requirements.txt /usr/test/requirements.txt
COPY .env /usr/test/.env

RUN chmod +x entrypoint.sh

RUN pip install -r requirements.txt

CMD [ "sh", "entrypoint.sh" ]