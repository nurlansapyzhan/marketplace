from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel


class ProductRead(BaseModel):
    id: int
    name: str
    brand_id: int
    description: str
    color_id: int
    product_rating: Optional[float]
    number_of_reviews: Optional[int]
    compound_id: int
    pattern_id: int
    season_id: int
    collection_id: int
    created_at: Optional[datetime]
    added_db_at: Optional[datetime]

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    id: int
    name: str
    brand_id: int
    description: str
    color_id: int
    product_rating: float
    compound_id: int
    pattern_id: int
    season_id: int
    collection_id: int
