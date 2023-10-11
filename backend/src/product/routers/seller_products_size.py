from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.product.schemas import SellerProductSizeRead, SellerProductSizeCreate
from src.product.models import SellerProductsSize

router = APIRouter(
    prefix="/seller_product_size",
    tags=["SellerProductsSize"]
)


@router.get("/", response_model=List[SellerProductSizeRead])
async def get_seller_product_size_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                                       page_size: Optional[int] = Query(10, description="Размер страницы", ge=1,
                                                                        le=100),
                                       session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(SellerProductsSize).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{seller_product_size_id}", response_model=SellerProductSizeRead)
async def get_seller_product_size_detail(seller_product_size_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(SellerProductsSize).filter_by(id=seller_product_size_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/")
async def post_seller_product_size_create(new_seller_product_size: SellerProductSizeCreate,
                                          session: AsyncSession = Depends(get_async_session)):
    stmt = insert(SellerProductsSize).values(**new_seller_product_size.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{seller_product_size_id}", response_model=SellerProductSizeCreate)
async def put_seller_product_size_update(seller_product_size_id: int, product: SellerProductSizeCreate,
                                         session: AsyncSession = Depends(get_async_session), ):
    stmt = (
        update(SellerProductsSize)
        .where(SellerProductsSize.id == seller_product_size_id)
        .values(**product.dict())
        .returning(SellerProductsSize)
    )
    result = await session.execute(stmt)
    updated_product = result.scalar()
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await session.commit()
    return updated_product


@router.delete("/{seller_product_size_id}", response_model=SellerProductSizeRead)
async def seller_product_size_delete(seller_product_size_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        update(SellerProductsSize)
        .where(SellerProductsSize.id == seller_product_size_id)
        .values({"is_deleted": True})
        .returning(SellerProductsSize)
    )
    result = await session.execute(stmt)
    delete_product = result.scalar()
    if delete_product is None:
        raise HTTPException(status_code=404, detail="Item not found")
    await session.commit()
    return delete_product
