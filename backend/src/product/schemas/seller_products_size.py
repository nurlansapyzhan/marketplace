from pydantic import BaseModel


class SellerProductSizeRead(BaseModel):
    id: int
    product_id: int
    size_numbers_id: int
    size_letter_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True


class SellerProductSizeCreate(BaseModel):
    product_id: int
    size_numbers_id: int
    size_letter_id: int
    quantity: int
    price: float




