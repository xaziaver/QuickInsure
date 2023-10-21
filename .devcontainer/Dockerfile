# Using the official Python 3.10 image as a base image
FROM python:3.10

# Updating and installing the PostgreSQL client and server
RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib \
    && apt-get clean

# Setting environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setting the working directory in the container
WORKDIR /app

# Copying the requirements.txt file from your host to your current location in the container
COPY requirements.txt /app/requirements.txt

# Installing any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
