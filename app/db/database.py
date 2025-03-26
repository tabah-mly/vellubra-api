from sqlmodel import SQLModel, create_engine, Session
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# Create database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session
