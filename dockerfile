FROM python:3.13.1-alpine3.21

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add --no-cache \
    gcc musl-dev python3-dev libffi-dev \
    nodejs npm \
    && pip install --upgrade pip \
    && rm -rf /var/cache/apk/*

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

RUN npm install -g npx

COPY ./ ./

run python manage.py makemigrations


