from pydantic import BaseModel


class AddressRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class AddressCreate(BaseModel):
    name: str
