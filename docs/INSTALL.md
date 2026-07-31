Installing the Hospital Management System
=====================================

**Prerequisites**

* Node.js and npm installed on your local machine
* PostgreSQL installed and running on your local machine
* Docker installed on your local machine

**Environment Setup**

1. Clone the repository: `git clone https://github.com/your-username/hospital-management-system.git`
2. Change into the project directory: `cd hospital-management-system`
3. Install dependencies: `npm install`

**Database Setup**

1. Create a new database: `createdb hospital_management`
2. Create a new user: `psql -U postgres -c "CREATE ROLE hospital_management WITH PASSWORD 'hospital_management';"`
3. Update the `config.py` file with your database credentials

**Backend Setup**

1. Run `pip install -r requirements.txt`
2. Update the `model.py` file with your database credentials

**Frontend Setup**

1. Run `npm start` to start the React.js development server

**Running Instructions**

1. Run `docker build -t hospital_management .`
2. Run `docker run -p 5432:5432 hospital_management`
3. Run `flask run` to start the Flask application
4. Run `npm start` to start the React.js development server