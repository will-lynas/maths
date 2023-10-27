# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm
WORKDIR /python-docker
COPY . .
RUN pip install -e ".[dev]"
RUN ./run_tests.sh
