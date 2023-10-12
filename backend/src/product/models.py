from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from datetime import datetime
from pytz import UTC

from src.auth.models import user

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
    is_deleted = Column(Boolean, default=False, nullable=False)


class Collection(Base):
    __tablename__ = "collection"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.timezone('UTC', utc_time))
    added_db_at = Column(DateTime, default=func.timezone('UTC', utc_time))


class Affiliation(Base):
    __tablename__ = "affiliation"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


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
    affiliation_id = Column(Integer, ForeignKey("affiliation.id"), nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)


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


class ProductSalesType(Base):
    __tablename__ = "product_sales_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class SellerProduct(Base):
    __tablename__ = "seller_product"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    salesman_id = Column(Integer, ForeignKey(user.c.id), nullable=False)
    discount = Column(Float, nullable=False)
    sale_type_id = Column(Integer, ForeignKey("product_sales_type.id"), nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    added_db_at = Column(DateTime, default=func.timezone('UTC', utc_time))
    deleted_at = Column(DateTime, nullable=True)


class SizeNumber(Base):
    __tablename__ = "size_numbers"

    id = Column(Integer, primary_key=True, index=True)
    size = Column(Integer, nullable=False)


class SizeLetter(Base):
    __tablename__ = "size_letter"

    id = Column(Integer, primary_key=True, index=True)
    size = Column(String, nullable=False)


class Size(Base):
    __tablename__ = "size"

    id = Column(Integer, primary_key=True, index=True)
    size_numbers_id = Column(Integer, ForeignKey("size_numbers.id"), nullable=False)
    size_letter_id = Column(Integer, ForeignKey("size_letter.id"), nullable=False)
    affiliation_id = Column(Integer, ForeignKey("affiliation.id"), nullable=False)


class SellerProductsSize(Base):
    __tablename__ = "seller_products_size"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    size_numbers_id = Column(Integer, ForeignKey("size_numbers.id"), nullable=True)
    size_letter_id = Column(Integer, ForeignKey("size_letter.id"), nullable=True)
    quantity = Column(Integer, nullable=True)
    price = Column(Float, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
