from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DiscountCouponRead(BaseModel):
    id: int
    name: str
    code: str
    discount_percentage: Optional[float]
    discount_amount: Optional[float]
    smallest_check_amount: Optional[float]
    largest_check_amount: Optional[float]
    total_number_activations: Optional[int]
    number_activations_per_user: Optional[int]
    is_deleted: bool
    coupon_start_date: Optional[datetime]
    coupon_expiration_date: Optional[datetime]
    coupon_creation_date: Optional[datetime]
    coupon_delete_date: Optional[datetime]

    class Config:
        orm_mode = True


class DiscountCouponCreate(BaseModel):
    name: str
    code: str
    discount_percentage: Optional[float]
    discount_amount: Optional[float]
    smallest_check_amount: Optional[float]
    largest_check_amount: Optional[float]
    total_number_activations: Optional[int]
    number_activations_per_user: Optional[int]
    coupon_start_date: Optional[datetime]
    coupon_expiration_date: Optional[datetime]
