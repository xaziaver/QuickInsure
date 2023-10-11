# Use an official Python runtime as the parent image
FROM python:3.10-slim-buster

# Set environment variables (these are examples; adjust as needed)
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql \
    postgresql-contrib \
    gcc \
    python3-dev \
    musl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

# Switch to a non-root user
RUN useradd -ms /bin/bash codespace
USER codespace

# Set working directory
WORKDIR /workspace
