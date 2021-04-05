FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt


ADD . /fast_app
WORKDIR /fast_app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
