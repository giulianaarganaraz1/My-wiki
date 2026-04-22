from fastapi import APIRouter
from app.models import Note

router = APIRouter()

notes_db = []

@router.get("/notes")
def get_notes():
    return notes_db

@router.post("/notes")
def create_note(note: Note):
    notes_db.append(note)
    return note

    