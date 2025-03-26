from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.schemas.user import UserCreate
from app.models.user import User, Token
from app.db.database import get_session
from app.core.security import create_access_token
import bcrypt

router = APIRouter()


@router.post("/signup/", response_model=Token)
def signup(user_data: UserCreate, session: Session = Depends(get_session)):
    existing_user = session.exec(
        select(User).where(User.username == user_data.username)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    user_data.hash_password()
    user = User(username=user_data.username, hashed_password=user_data.password)
    session.add(user)
    session.commit()
    session.refresh(user)

    access_token = create_access_token(
        {"sub": str(user.id)}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or not bcrypt.checkpw(
        form_data.password.encode(), user.hashed_password.encode()
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    access_token = create_access_token(
        {"sub": str(user.id)}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}
