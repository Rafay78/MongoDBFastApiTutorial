from fastapi import APIRouter
from models.note import Note
from config.db import conn
from typing import Union
from schemas.note import NoteEntity, NotesEntity

note = APIRouter()

@note.get("/")
def read_root():
    return NoteEntity(conn.EventManagementSystem.users.find_one({}))

@note.get("/all")
def read_roots():
    return NotesEntity(conn.EventManagementSystem.users.find({}))

@note.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}