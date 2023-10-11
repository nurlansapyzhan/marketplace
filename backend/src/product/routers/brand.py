from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.product.schemas import BrandCreate, BrandRead
from src.product.models import Brand
from src.database import get_async_session

router = APIRouter(
    prefix="/brand",
    tags=["Brand"]
)


@router.get("/", response_model=List[BrandRead])
async def get_brand_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                           page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                           session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Brand).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{brand_id}", response_model=BrandRead)
async def get_brand_detail(brand_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Brand).filter_by(id=brand_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/")
async def post_brand_create(new_brand: BrandCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Brand).values(**new_brand.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{brand_id}", response_model=BrandCreate)
async def put_brand_update(brand_id: int, brand: BrandCreate, session: AsyncSession = Depends(get_async_session), ):
    stmt = (
        update(Brand)
        .where(Brand.id == brand_id)
        .values(**brand.dict())
        .returning(Brand)
    )
    result = await session.execute(stmt)
    updated_product = result.scalar()
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await session.commit()
    return updated_product


@router.delete("/{brand_id}", response_model=BrandRead)
async def brand_delete(brand_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        update(Brand)
        .where(Brand.id == brand_id)
        .values({"is_deleted": True})
        .returning(Brand)
    )
    result = await session.execute(stmt)
    delete_product = result.scalar()
    if delete_product is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await session.commit()
    return delete_product


