from fastapi import APIRouter, HTTPException, Body
from typing import List
from schemas import Note, NoteCreate
import os
from dotenv import load_dotenv
import google.generativeai as genai

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

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

@router.post("/notes/{note_id}/summary")
def summarize_note(note_id: int):
    for note in notes_db:
        if note.id == note_id:
            prompt = f"Summarize this note:\nTitle: {note.title}\nContent: {note.content}"
            response = model.generate_content(contents=prompt)
            return {"summary": response.text}
    raise HTTPException(status_code=404, detail="Note not found")

@router.post("/notes/{note_id}/qa")
def question_answer(note_id: int, question: str = Body(..., embed=True)):
    for note in notes_db:
        if note.id == note_id:
            prompt = f"Note:\nTitle: {note.title}\nContent: {note.content}\nQuestion: {question}"
            response = model.generate_content(contents=prompt)
            return {"answer": response.text}
    raise HTTPException(status_code=404, detail="Note not found")