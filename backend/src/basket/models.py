from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from datetime import datetime
from pytz import UTC

from src.auth.models import user

from src.product.models import Product

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


class DiscountCoupon(Base):
    __tablename__ = "discount_coupon"

    id = Column(Integer, primary_key=True, index=True)
    name_coupons = Column(String, nullable=False)
    coupon_code = Column(String, nullable=False)
    discount_percentage = Column(Float, nullable=True)
    discount_amount = Column(Float, nullable=True)
    smallest_check_amount = Column(Float, nullable=True)
    largest_check_amount = Column(Float, nullable=True)
    total_number_activations = Column(Integer, nullable=True)
    number_activations_per_user = Column(Integer, nullable=True)
    is_deleted = Column(Boolean, default=False, nullable=False)
    coupon_start_date = Column(DateTime, nullable=True)
    coupon_expiration_date = Column(DateTime, nullable=True)
    coupon_creation_date = Column(DateTime, default=func.timezone('UTC', utc_time))
    coupon_delete_date = Column(DateTime, nullable=True)


class UsersCoupon(Base):
    __tablename__ = "users_coupon"

    id = Column(Integer, primary_key=True, index=True)
    seller_who_provides_coupon_id = Column(Integer, ForeignKey(user.c.id), nullable=True)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=True)
    buyer_who_can_use_coupon_id = Column(Integer, ForeignKey(user.c.id), nullable=True)
    coupon_id = Column(Integer, ForeignKey('discount_coupon.id'), nullable=False)


class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, index=True)
    notification_title = Column(String, nullable=False)
    notification_text = Column(String, nullable=False)


class OrderStatus(Base):
    __tablename__ = "order_status"

    id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String, nullable=False)
    notification_status_id = Column(Integer, ForeignKey('notification.id'), nullable=False)


class OrderDeliveryStatus(Base):
    __tablename__ = "order_delivery_status"

    id = Column(Integer, primary_key=True, index=True)
    check_id = Column(Integer, ForeignKey('check.id'), nullable=False)
    order_status_id = Column(Integer, ForeignKey('order_status.id'), nullable=False)
    date_presentation_status = Column(DateTime, default=func.timezone('UTC', utc_time))
