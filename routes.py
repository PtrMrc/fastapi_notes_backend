from fastapi import APIRouter, HTTPException
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

@router.get("/noted/{note_id}", response_model=Note)
def get_note(note_id: int):
    for note in notes_db:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

@router.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, updated_note: NoteCreate):
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db[index] = Note(id=note_id, **updated_note.model_dump())
            return notes_db[index]
    raise HTTPException(status_code=404, detail="Note not found")

@router.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            deleted_note = notes_db.pop(index)
            return {"message": "Note deleted", "note": delete_note}
    raise HTTPException(status_code=404, detail="Note not found")
