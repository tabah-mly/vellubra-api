from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse
from app.db.database import get_session
import uuid
from datetime import datetime, timezone

router = APIRouter()


@router.post("/", response_model=NoteResponse)
def create_note(
    note_data: NoteCreate,
    session: Session = Depends(get_session),
):
    now = datetime.now(timezone.utc)
    note = Note(
        **note_data.model_dump(),
        created_at=now,
        updated_at=now,
    )
    session.add(note)
    session.commit()
    session.refresh(note)
    return note


@router.get("/", response_model=list[NoteResponse])
def read_notes(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    notes = session.exec(select(Note).offset(offset).limit(limit)).all()
    return [NoteResponse.model_validate(note) for note in notes]


@router.put("/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: uuid.UUID,
    note_data: NoteCreate,
    session: Session = Depends(get_session),
):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    for key, value in note_data.model_dump(exclude_unset=True).items():
        setattr(note, key, value)
    note.updated_at = datetime.now(timezone.utc)

    session.commit()
    session.refresh(note)
    return note


@router.get("/{note_id}", response_model=NoteResponse)
def read_note(
    note_id: uuid.UUID,
    session: Session = Depends(get_session),
):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.delete("/{note_id}")
def delete_note(
    note_id: uuid.UUID,
    session: Session = Depends(get_session),
):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    session.delete(note)
    session.commit()
    return {"ok": True}
