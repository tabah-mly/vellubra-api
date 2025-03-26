from sqlmodel import SQLModel, Field
import uuid


class Token(SQLModel):
    access_token: str
    token_type: str


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str
