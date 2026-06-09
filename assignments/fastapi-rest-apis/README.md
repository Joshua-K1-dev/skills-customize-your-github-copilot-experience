# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI and Python. You will create endpoints that return data, accept requests, and use validation to make the API reliable and easy to use.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description
Set up a working FastAPI app and define the first endpoint for your API.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Add a root endpoint that returns a helpful welcome message
- Define at least one Pydantic model for the data your API will manage

### 🛠️ Build RESTful CRUD endpoints

#### Description
Implement endpoints that let users create, view, update, and delete records.

#### Requirements
Completed program should:

- Support `GET`, `POST`, `PUT`, and `DELETE` operations for one resource type
- Use path parameters and request bodies correctly
- Return the right status codes for successful requests and missing records

### 🛠️ Add validation and query features

#### Description
Improve your API so it handles bad input and supports simple filtering or searching.

#### Requirements
Completed program should:

- Validate incoming data with Pydantic
- Return clear error responses when a request is invalid
- Support at least one query parameter for filtering or searching results
