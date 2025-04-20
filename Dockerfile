# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV POETRY_VERSION=1.8.2 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential curl && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy only requirements to cache dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Entrypoint
CMD ["uvicorn", "nistaiapp.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
