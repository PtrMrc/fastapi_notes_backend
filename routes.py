from fastapi import APIRouter
from typing import List
from schemas import Note, NoteCreate

router = APIRouter()

notes_db = []
note_id_counter = 1

@router.get("/notes", response_model=List[Note])
def get_notes():
    return notes_db

@router.post("/notes", response_model=Note)
def create_note(note: NoteCreate):
    global note_id_counter
    new_note = Note(id=note_id_counter, **note.model_dump())
    note_id_counter += 1
    notes_db.append(new_note)
    return new_note

