# Dockerfile for main_service
FROM python:3.11.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # Install dockerize
# RUN wget https://github.com/jwilder/dockerize/releases/latest/download/dockerize-linux-amd64.tar.gz && \
#     tar -C /usr/local/bin -xzvf dockerize-linux-amd64.tar.gz && \
#     rm dockerize-linux-amd64.tar.gz

WORKDIR /app

COPY requirements.txt /app/main_requirements.txt

RUN pip install --no-cache-dir -r main_requirements.txt

COPY . /app/
