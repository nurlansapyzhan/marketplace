from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from datetime import datetime
from pytz import UTC

from src.auth.models import user

Base = declarative_base()
utc_time = datetime(2023, 9, 22, 11, 12, 41, 530000, tzinfo=UTC)


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    address_name = Column(String, nullable=False)


class PaymentMethods(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True, index=True)
    method_names = Column(String, nullable=False)


class Check(Base):
    __tablename__ = "check"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey(user.c.id), nullable=False)
    address_id = Column(Integer, ForeignKey('address.id'), nullable=False)
    total_price = Column(Float, nullable=True)
    delivery_price = Column(Float, nullable=True)
    method_names_id = Column(Integer, ForeignKey('payment_methods.id'), nullable=True)
    basket_created_at = Column(DateTime, default=func.timezone('UTC', utc_time))
    check_created_at = Column(DateTime, nullable=True)
