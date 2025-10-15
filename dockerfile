FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --no-install-recommends \
    gcc \
    build-essential \
    libffi-dev \
    libpq-dev \
    python3-dev \
    nodejs \
    npm \
    && pip install --upgrade pip \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

RUN npm install -g npx

COPY ./ ./



