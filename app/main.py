from fastapi import FastAPI
from app.db.database import create_db_and_tables
from contextlib import asynccontextmanager
from app.routes import note


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(note.router, prefix="/notes", tags=["Notes"])
