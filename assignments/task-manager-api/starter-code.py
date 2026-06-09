"""Starter code for the Task Manager API with FastAPI and SQLite."""

import sqlite3
from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

DATABASE = "tasks.db"
app = FastAPI(title="Task Manager API")


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class Task(TaskCreate):
    id: int


def get_connection():
    return sqlite3.connect(DATABASE)


def create_tables():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


create_tables()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API assignment."}


@app.get("/tasks")
def get_tasks(completed: Optional[bool] = None):
    # TODO: Read tasks from SQLite and optionally filter them.
    return []


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Fetch one task from SQLite or raise a 404 error.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # TODO: Insert a task into SQLite and return the created record.
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    # TODO: Update the task in SQLite and return the updated record.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the task from SQLite and confirm the deletion.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
