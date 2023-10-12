from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ColorRead(BaseModel):
    id: int
    color_name: str
    number_color: int

    class Config:
        orm_mode = True


class CompoundRead(BaseModel):
    id: int
    compound_name: str

    class Config:
        orm_mode = True


class PatternRead(BaseModel):
    id: int
    patterns_name: str

    class Config:
        orm_mode = True


class CollectionRead(BaseModel):
    id: int
    name: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class AffiliationRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategoryRead(BaseModel):
    id: int
    category: str
    category_id: Optional[int]

    class Config:
        orm_mode = True


class ProductCategoryRead(BaseModel):
    id: int
    product_id: int
    category_id: int

    class Config:
        orm_mode = True


class ProductSalesTypeRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SizeNumberRead(BaseModel):
    id: int
    size: int

    class Config:
        orm_mode = True


class SizeLetterRead(BaseModel):
    id: int
    size: str

    class Config:
        orm_mode = True


class SizeRead(BaseModel):
    id: int
    size_numbers_id: int
    size_letter_id: int
    affiliation_id: int

    class Config:
        orm_mode = True


class SeasonRead(BaseModel):
    id: int
    seasons_name: str

    class Config:
        orm_mode = True
