# 📝 FastAPI Notes Backend

A simple backend built with **FastAPI** for managing notes.  
It supports full **CRUD operations** and integrates with **Google Gemini AI** for smart features like summarization and Q&A.

---

## 🚀 Features

- ✅ Create, read, update, and delete notes (CRUD)
- ✅ Interactive API docs at `/docs`
- 🤖 AI-powered **note summarization**
- 🤖 AI-powered **Q&A about notes**

---

## 📖 API Endpoints

| Method | Endpoint              | Description                         |
|--------|-----------------------|-------------------------------------|
| GET    | `/notes`              | List all notes                      |
| POST   | `/notes`              | Create a new note                   |
| GET    | `/notes/{id}`         | Retrieve a note by ID               |
| PUT    | `/notes/{id}`         | Update a note by ID                 |
| DELETE | `/notes/{id}`         | Delete a note by ID                 |
| POST   | `/notes/{id}/summary` | Summarize a note with AI            |
| POST   | `/notes/{id}/qa`      | Ask a question about a note with AI |

---

## 🛠️ Tech Stack
- Python
- FastAPI
- Pydantic
- Google Gemini

