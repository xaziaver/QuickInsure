# QuickInsure

A Simple Property Insurance Quotation System

## Prerequisites

- Python 3.7+ (recommended to use a virtual environment)
- PostgreSQL 10+ 

## Setup

1. **Clone the Repository**:
   
   git clone https://github.com/xaziaver/QuickInsure.git
   cd QuickInsure

2. **Set Up Virtual Environment**:

   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Python Dependencies**:

   pip install -r requirements.txt

4. **Set Up PostgreSQL**:
   
   - Ensure PostgreSQL is installed and running.
   - Create a new database and user with the following default credentials:
     - Database Name: `DATA`
     - User: `admin`
     - Password: `admin`
   - Grant necessary permissions.
   - Configure the connection details either by setting environment variables (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`) or by editing the `settings.py` file.
   
   For example, if using the PostgreSQL command-line tools:

   createdb DATA
   createuser admin -W  # Will prompt for a password. Enter 'admin'.
   psql -c "GRANT ALL PRIVILEGES ON DATABASE DATA TO admin;"

5. **Run Migrations and Start the App**:

   python manage.py migrate
   python manage.py runserver

Visit `http://127.0.0.1:8000/` in your browser to access the app.