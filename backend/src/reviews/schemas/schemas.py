from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReviewRead(BaseModel):
    id: int
    user_who_left_review_id: int
    to_the_seller_id: Optional[int]
    product_id: Optional[int]
    review_id: Optional[int]
    review_text: Optional[str]
    grade: Optional[float]
    added_db_at: datetime
    is_deleted: bool
    deleted_at: Optional[datetime]


class ReviewCreate(BaseModel):
    user_who_left_review_id: int
    to_the_seller_id: Optional[int]
    product_id: Optional[int]
    review_id: Optional[int]
    review_text: Optional[str]
    grade: Optional[float]
