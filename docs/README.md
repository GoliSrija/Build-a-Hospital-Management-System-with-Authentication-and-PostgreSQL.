Hospital Management System with Authentication and PostgreSQL
=====================================================

**Project Description**

This is a comprehensive software development project that aims to create a scalable and secure system for managing patient and staff data, medical records, and billing and insurance information.

**Features**

* Patient registration and verification
* Medical history management
* Appointment scheduling
* Medication management
* Staff registration and verification
* Employee scheduling
* Patient communication management
* User management
* System settings configuration

**Technologies Used**

* PostgreSQL
* Node.js
* Express.js
* React.js
* Flask
* Flask-SQLAlchemy
* Psycopg2-binary
* Docker

**Folder Structure**

* **app**
	+ **__init__.py**
	+ **app.py**
	+ **config.py**
	+ **models.py**
	+ **routes.py**
	+ **templates**
	+ **static**
* **database**
	+ **schema.sql**
	+ **sample_data.sql**
* **.gitignore**
* **Dockerfile**

**Installation Steps**

1. Install Node.js and npm: `brew install node`
2. Install PostgreSQL: `brew install postgres`
3. Create a new database: `createdb hospital_management`
4. Create a new user: `psql -U postgres -c "CREATE ROLE hospital_management WITH PASSWORD 'hospital_management';"`
5. Install Python and pip: `brew install python`
6. Install Flask and Flask-SQLAlchemy: `pip install flask flask-sqlalchemy`
7. Install Psycopg2-binary: `pip install psycopg2-binary`
8. Run `pip install -r requirements.txt`
9. Create a new file `config.py` and add your database credentials: `DATABASE_USER = 'hospital_management'`, `DATABASE_PASSWORD = 'hospital_management', `DATABASE_HOST = 'localhost'`, `DATABASE_NAME = 'hospital_management'`
10. Run `docker build -t hospital_management .`

**Running the Project**

1. Run `docker run -p 5432:5432 hospital_management`
2. Run `flask run` to start the Flask application
3. Run `npm start` to start the React.js development server

**API Overview**

* `/users`: GET, POST, PUT, DELETE
* `/posts`: GET, POST
* `/comments`: GET, POST