from pydantic import BaseModel


class BrandRead(BaseModel):
    id: int
    brand_name: str

    class Config:
        orm_mode = True


class BrandCreate(BaseModel):
    brand_name: str




