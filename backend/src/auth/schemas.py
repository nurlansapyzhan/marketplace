import uuid
from typing import Optional

from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    def create_update_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }


class UserUpdate(BaseModel):
    username: str
    password: str
