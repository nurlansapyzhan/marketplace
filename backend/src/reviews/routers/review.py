from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.reviews.models import Review
from src.reviews.schemas import ReviewRead, ReviewCreate

router = APIRouter(
    prefix="/review",
    tags=["Reviews"]
)


@router.get("/", response_model=List[ReviewRead])
async def get_review_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                          page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                          session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Review).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{review_id}", response_model=ReviewRead)
async def get_review_detail(review_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Review).filter_by(id=review_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/")
async def post_review_create(new_review: ReviewCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Review).values(**new_review.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{review_id}", response_model=ReviewCreate)
async def put_review_update(review_id: int, product: ReviewCreate,
                            session: AsyncSession = Depends(get_async_session), ):
    stmt = (
        update(Review)
        .where(Review.id == review_id)
        .values(**product.dict())
        .returning(Review)
    )
    result = await session.execute(stmt)
    updated_review = result.scalar()
    if updated_review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    await session.commit()
    return updated_review


@router.delete("/{review_id}", response_model=ReviewRead)
async def review_delete(review_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        update(Review)
        .where(Review.id == review_id)
        .values({"is_deleted": True})
        .returning(Review)
    )
    result = await session.execute(stmt)
    delete_review = result.scalar()
    if delete_review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    await session.commit()
    return delete_review
