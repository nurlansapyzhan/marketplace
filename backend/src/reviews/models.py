from pytz import UTC
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean

from src.auth.models import user

from src.product.models import Product

Base = declarative_base()
utc_time = datetime(2023, 9, 22, 11, 12, 41, 530000, tzinfo=UTC)


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    user_who_left_review_id = Column(Integer, ForeignKey(user.c.id), nullable=False)
    to_the_seller_id = Column(Integer, ForeignKey(user.c.id), nullable=True)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=True)
    review_id = Column(Integer, ForeignKey('review.id'), nullable=True)
    review_text = Column(String, nullable=True)
    grade = Column(Float, nullable=True)
    added_db_at = Column(DateTime, default=func.timezone('UTC', utc_time))
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
