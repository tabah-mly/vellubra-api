from sqlmodel import SQLModel
import uuid
from datetime import datetime


class NoteCreate(SQLModel):
    title: str
    content: str | None = None
    tags: str | None = None
    published: bool = False


class NoteResponse(NoteCreate):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
