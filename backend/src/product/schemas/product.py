from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from typing import List
from fastapi import UploadFile

from src.product.schemas.photo import PhotoRead, PhotoCreate


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


class ProductListRead(BaseModel):
    id: int
    name: str
    brand_id: int
    color_id: int
    product_rating: Optional[float]
    number_of_reviews: Optional[int]
    compound_id: int
    pattern_id: int
    season_id: int
    collection_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: str
    brand_id: int
    description: str
    color_id: int
    compound_id: int
    pattern_id: int
    season_id: int
    collection_id: int
    affiliation_id: int


class ProductPut(BaseModel):
    name: str
    brand_id: int
    description: str
    color_id: int
    compound_id: int
    pattern_id: int
    season_id: int
    collection_id: int
    affiliation_id: int


class ProductPhoto(ProductListRead):
    photo: Optional[List[PhotoRead]]


class ProductPhotoCreate(ProductCreate):
    photo: UploadFile

