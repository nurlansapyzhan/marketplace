from pydantic import BaseModel
from typing import Optional


class SellerProductSizeRead(BaseModel):
    id: int
    product_id: int
    size_numbers_id: Optional[int]
    size_letter_id: Optional[int]
    quantity: Optional[int]
    price: float

    class Config:
        orm_mode = True


class SellerProductSizeCreate(BaseModel):
    product_id: int
    size_numbers_id: Optional[int]
    size_letter_id: Optional[int]
    quantity: Optional[int]
    price: float




