Hospital Management System API Documentation
=====================================

**API Endpoints**

* **GET /users**: Retrieves a list of all users
* **POST /users**: Creates a new user
* **GET /posts**: Retrieves a list of all posts
* **POST /posts**: Creates a new post
* **GET /comments**: Retrieves a list of all comments
* **POST /comments**: Creates a new comment

**HTTP Methods**

* GET: Retrieve a resource
* POST: Create a new resource
* PUT: Update a resource
* DELETE: Delete a resource

**Request Format**

* All requests will be in JSON format
* All requests will have a JSON body with the required information

**Response Format**

* All responses will be in JSON format
* Responses will contain a JSON object with a success or error message

**Error Codes**

* 400: Bad Request
* 401: Unauthorized
* 422: Unprocessable Entity
* 500: Internal Server Error