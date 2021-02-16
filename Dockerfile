FROM python:3.7-slim-buster AS base
LABEL maintainer="Espoir Murhabazi <try to look it@ for yourself>"

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

RUN python -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# i run this to fix the issue connecting to mysql server 

RUN useradd --create-home esp_py
WORKDIR /home/esp_py
USER esp_py

COPY . .
