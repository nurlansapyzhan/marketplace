from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.basket.models import DiscountCoupon
from src.basket.schemas.discount_coupon import DiscountCouponRead, DiscountCouponCreate

router = APIRouter(
    prefix="/discount-coupon",
    tags=["Discount coupon"]
)


@router.get("/", response_model=List[DiscountCouponRead])
async def get_discount_coupon_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                                   page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                                   session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(DiscountCoupon).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{discount_coupon_id}", response_model=DiscountCouponRead)
async def get_discount_coupon_detail(discount_coupon_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(DiscountCoupon).filter_by(id=discount_coupon_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/")
async def post_discount_coupon_create(new_discount_coupon: DiscountCouponCreate,
                                      session: AsyncSession = Depends(get_async_session)):
    stmt = insert(DiscountCoupon).values(**new_discount_coupon.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{discount_coupon_id}", response_model=DiscountCouponCreate)
async def put_discount_coupon_update(discount_coupon_id: int, product: DiscountCouponCreate,
                             session: AsyncSession = Depends(get_async_session), ):
    stmt = (
        update(DiscountCoupon)
        .where(DiscountCoupon.id == discount_coupon_id)
        .values(**product.dict())
        .returning(DiscountCoupon)
    )
    result = await session.execute(stmt)
    updated_discount_coupon = result.scalar()
    if updated_discount_coupon is None:
        raise HTTPException(status_code=404, detail="Discount coupon not found")

    await session.commit()
    return updated_discount_coupon


@router.delete("/{discount_coupon_id}", response_model=DiscountCouponRead)
async def discount_coupon_delete(discount_coupon_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        update(DiscountCoupon)
        .where(DiscountCoupon.id == discount_coupon_id)
        .values({"is_deleted": True})
        .returning(DiscountCoupon)
    )
    result = await session.execute(stmt)
    delete_discount_coupon = result.scalar()
    if delete_discount_coupon is None:
        raise HTTPException(status_code=404, detail="Discount coupon not found")

    await session.commit()
    return delete_discount_coupon
