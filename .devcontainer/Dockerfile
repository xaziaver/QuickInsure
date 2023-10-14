FROM python:3.10

# Install PostgreSQL client
RUN apt-get update \
    && apt-get install -y postgresql-client \
    && apt-get clean

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /

# Copy the requirements.txt file into the Docker image
COPY ../requirements.txt requirements.txt

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt
