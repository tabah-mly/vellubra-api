from sqlmodel import SQLModel
import bcrypt


class UserCreate(SQLModel):
    username: str
    password: str

    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode()
