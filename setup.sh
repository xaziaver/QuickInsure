#!/bin/bash

# Stop the script if any command fails
set -e

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py migrate

# Provide a message to indicate setup completion
echo "Setup complete. Activate the virtual environment with 'source venv/bin/activate', then run the server with 'python manage.py runserver'."
