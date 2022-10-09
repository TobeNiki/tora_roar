FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 
COPY requirements.txt /root/

WORKDIR /root/
RUN pip install -r requirements.txt
