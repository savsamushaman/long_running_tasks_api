FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD . /fast_app
WORKDIR /fast_app

CMD hypercorn main:app --reload
