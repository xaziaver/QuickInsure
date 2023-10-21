#!/bin/bash

# Starting the PostgreSQL service
service postgresql start

# Configuring the database
sudo -u postgres psql -c "CREATE DATABASE DATA;"
sudo -u postgres psql -c "CREATE USER admin WITH PASSWORD 'admin';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE DATA TO admin;"