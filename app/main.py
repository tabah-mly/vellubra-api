from fastapi import FastAPI
from app.db.database import create_db_and_tables
from contextlib import asynccontextmanager
from app.routes import note, auth, docs
from app.utils.custom_openapi import custom_openapi


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    lifespan=lifespan,
    docs_url=None,  # Disable Swagger UI (/docs)
    redoc_url=None,  # Disable ReDoc (/redoc)
)

app.include_router(docs.router, tags=["Docs"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(note.router, prefix="/notes", tags=["Notes"])

app.openapi = lambda: custom_openapi(app)
