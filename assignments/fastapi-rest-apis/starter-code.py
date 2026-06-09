"""Starter code for Building REST APIs with FastAPI."""

from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    completed: bool = False


items: List[Item] = [
    Item(id=1, name="Set up FastAPI", description="Install dependencies and create the app"),
    Item(id=2, name="Build endpoints", description="Add CRUD routes for the resource"),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment."}


@app.get("/items")
def get_items():
    # TODO: Return all items.
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Return one item by ID or raise a 404 error if it is missing.
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    # TODO: Add a new item to the collection.
    items.append(item)
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    # TODO: Update an existing item and return the updated record.
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: Remove an item by ID and confirm the deletion.
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(index)
            return {"deleted": deleted_item.id}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
