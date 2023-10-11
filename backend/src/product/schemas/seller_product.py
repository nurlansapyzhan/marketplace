from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SellerProductRead(BaseModel):
    id: int
    product_id: int
    salesman_id: int
    discount: float
    sale_type_id: int
    added_db_at: Optional[datetime]

    class Config:
        orm_mode = True


class SellerProductCreate(BaseModel):
    product_id: int
    salesman_id: int
    discount: float
    sale_type_id: int




