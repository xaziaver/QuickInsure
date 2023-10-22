#!/bin/bash

# Dynamically locating the path to the PostgreSQL binaries
PG_BIN_PATH=$(find /usr -name pg_ctl | xargs dirname)
export PATH=$PG_BIN_PATH:$PATH

# Starting the PostgreSQL service
service postgresql start

# Wait until the PostgreSQL service is ready
until pg_isready; do
    echo "Waiting for PostgreSQL to start..."
    sleep 1
done

su - postgres -c "psql -c \"CREATE DATABASE data;\""
su - postgres -c "psql -c \"CREATE USER admin WITH PASSWORD 'admin_password';\""
su - postgres -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE data TO admin;\""
su - postgres -c "psql -c \"ALTER USER admin CREATEDB;\""
su - postgres -c "psql data -c \"GRANT ALL PRIVILEGES ON SCHEMA public TO admin;\""

# Making migrations
python manage.py makemigrations

# Running migrations
python manage.py migrate

# Automatically creating a superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('txt', '', 'pass')" | python manage.py shell