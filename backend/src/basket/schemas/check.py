from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CheckRead(BaseModel):
    id: int
    buyer_id: int
    address_id: int
    total_price: Optional[float]
    delivery_price: Optional[float]
    payment_methods_id: Optional[int]
    basket_created_at: datetime
    check_created_at: Optional[datetime]



class CheckCreate(BaseModel):
    buyer_id: int
    address_id: int
    total_price: Optional[float]
    delivery_price: Optional[float]
    payment_methods_id: Optional[int]
