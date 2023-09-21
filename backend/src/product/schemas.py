from pydantic import BaseModel


class ProductRead(BaseModel):
    id: int
    name: str
    brand_id: int
    description: str
    collor_id: int
    product_rating: float
    number_of_reviews: float
    compound_id: int
    pattern_id: int
    season_id: int
    collection_id: int

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    id: int
    name: str
    brand_id: int
    description: str
    collor_id: int
    product_rating: float
    number_of_reviews: float
    compound_id: int
    pattern_id: int
    season_id: int
    collection_id: int
