from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from datetime import datetime
from pytz import UTC

Base = declarative_base()
utc_time = datetime(2023, 9, 22, 11, 12, 41, 530000, tzinfo=UTC)


class Color(Base):
    __tablename__ = "color"

    id = Column(Integer, primary_key=True, index=True)
    color_name = Column(String, nullable=False)
    number_color = Column(Integer, nullable=False)


class Compound(Base):
    __tablename__ = "compound"

    id = Column(Integer, primary_key=True, index=True)
    compound_name = Column(String, nullable=False)


class Pattern(Base):
    __tablename__ = "pattern"

    id = Column(Integer, primary_key=True, index=True)
    patterns_name = Column(String, nullable=False)


class Season(Base):
    __tablename__ = "season"

    id = Column(Integer, primary_key=True, index=True)
    seasons_name = Column(String, nullable=False)


class Brand(Base):
    __tablename__ = "brand"

    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String, nullable=False)


class Collection(Base):
    __tablename__ = "collection"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.timezone('UTC', utc_time))
    added_db_at = Column(DateTime, default=func.timezone('UTC', utc_time))


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brand_id = Column(Integer, ForeignKey("brand.id"), nullable=True)
    description = Column(String, nullable=True)
    color_id = Column(Integer, ForeignKey("color.id"), nullable=True)
    product_rating = Column(Float, nullable=True)
    number_of_reviews = Column(Integer, nullable=True)
    compound_id = Column(Integer, ForeignKey("compound.id"), nullable=True)
    pattern_id = Column(Integer, ForeignKey("pattern.id"), nullable=True)
    season_id = Column(Integer, ForeignKey("season.id"), nullable=True)
    collection_id = Column(Integer, ForeignKey("collection.id"), nullable=True)
    created_at = Column(DateTime, default=func.timezone('UTC', utc_time))
    added_db_at = Column(DateTime, default=func.timezone('UTC', utc_time))


class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=True)


class ProductCategory(Base):
    __tablename__ = "product_category"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
