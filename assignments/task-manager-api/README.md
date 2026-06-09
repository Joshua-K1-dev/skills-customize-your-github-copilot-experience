# 📘 Assignment: Task Manager API with FastAPI and SQLite

## 🎯 Objective

Build a task manager REST API using FastAPI and SQLite. You will create endpoints that store tasks in a database, support common CRUD operations, and let users filter tasks with query parameters.

## 📝 Tasks

### 🛠️ Set up the API and database

#### Description
Create a FastAPI application that connects to a SQLite database and prepares the task table.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Connect to a SQLite database using Python's built-in `sqlite3` module
- Create a table for storing tasks if it does not already exist
- Include a root endpoint that returns a welcome message

### 🛠️ Build CRUD endpoints for tasks

#### Description
Implement endpoints that let users create, read, update, and delete tasks.

#### Requirements
Completed program should:

- Support `GET`, `POST`, `PUT`, and `DELETE` operations for tasks
- Store task data in SQLite instead of in-memory variables
- Return `404` responses when a task is not found
- Return appropriate status codes for successful create and update requests

### 🛠️ Add filtering and validation

#### Description
Improve the API so it handles bad input and supports simple search or filtering.

#### Requirements
Completed program should:

- Validate request data with Pydantic models
- Support at least one query parameter for filtering tasks, such as by completion status
- Return clear error messages for invalid requests
- Keep task fields consistent across database reads and writes
