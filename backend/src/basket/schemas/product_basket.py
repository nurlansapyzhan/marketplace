from pydantic import BaseModel


class ProductBasketRead(BaseModel):
    id: int
    check_id: int
    product_id: int
    quantity: int
    total_price: float
    coupon_id: int
    total_price_with_coupon: float

    class Config:
        orm_mode = True


class ProductBasketCreate(BaseModel):
    check_id: int
    product_id: int
    quantity: int
    total_price: float
    coupon_id: int
    total_price_with_coupon: float




