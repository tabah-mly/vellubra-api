from fastapi import FastAPI
from app.db.database import create_db_and_tables
from contextlib import asynccontextmanager
from app.routes import note, auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(note.router, prefix="/notes", tags=["Notes"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
