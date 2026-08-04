FROM python:3.10-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential libffi-dev ffmpeg aria2 python3-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt pytube

ENV COOKIES_FILE_PATH="youtube_cookies.txt"

CMD ["sh","-c","gunicorn app:app & python3 main.py"]
