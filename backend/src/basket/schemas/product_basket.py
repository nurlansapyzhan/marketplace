from pydantic import BaseModel
from typing import Optional


class ProductBasketRead(BaseModel):
    id: int
    check_id: int
    product_id: int
    quantity: int
    total_price: float
    coupon_id: Optional[int]
    total_price_with_coupon: Optional[float]

    class Config:
        orm_mode = True


class ProductBasketCreate(BaseModel):
    check_id: int
    product_id: int
    quantity: int
    total_price: float
    coupon_id: Optional[int]
    total_price_with_coupon: Optional[float]




