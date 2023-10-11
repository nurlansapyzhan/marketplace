from pydantic import BaseModel


class PhotoRead(BaseModel):
    id: int
    url: str
    product_id: int

    class Config:
        orm_mode = True


class PhotoCreate(BaseModel):
    url: str
    product_id: int
