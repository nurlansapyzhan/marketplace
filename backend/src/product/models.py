from enum import Enum

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Collor(Base):
    __tablename__ = "collors"

    id = Column(Integer, primary_key=True, index=True)
    collor_name = Column(String, index=True)
    number_collor = Column(Integer, nullable=False)


class Compound(Base):
    __tablename__ = "compounds"

    id = Column(Integer, primary_key=True, index=True)
    compound_name = Column(String, index=True)


class Pattern(Base):
    __tablename__ = "patterns"

    id = Column(Integer, primary_key=True, index=True)
    patterns_name = Column(String, index=True)


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, index=True)
    seasons_name = Column(String, index=True)


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String, index=True)


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    description = Column(String, nullable=True)
    collor_id = Column(Integer, ForeignKey("collors.id"))
    product_rating = Column(Float)
    number_of_reviews = Column(Float)
    compound_id = Column(Integer, ForeignKey("compounds.id"))
    pattern_id = Column(Integer, ForeignKey("patterns.id"))
    season_id = Column(Integer, ForeignKey("seasons.id"))
    collection_id = Column(Integer, ForeignKey("collections.id"))

