from typing import Optional

from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    name: Optional[str]
    address: Optional[int]
    phone: Optional[str]
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    name: Optional[str]
    email: EmailStr
    password: str

    def create_update_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "name": self.name
        }


class UserUpdate(BaseModel):
    username: Optional[str]
    name: Optional[str]
    address: Optional[int]
    phone: Optional[str]
