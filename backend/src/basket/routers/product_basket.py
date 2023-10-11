from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.basket.models import ProductsBasket
from src.basket.schemas import ProductBasketRead, ProductBasketCreate

router = APIRouter(
    prefix="/product_basket",
    tags=["ProductsBasket"]
)


@router.get("/", response_model=List[ProductBasketRead])
async def get_brand_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                           page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                           session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(ProductsBasket).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{product_basket_id}", response_model=ProductBasketRead)
async def get_brand_detail(product_basket_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(ProductsBasket).filter_by(id=product_basket_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/")
async def post_brand_create(new_product_basket: ProductBasketCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(ProductsBasket).values(**new_product_basket.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{product_basket_id}", response_model=ProductBasketCreate)
async def put_brand_update(product_basket_id: int, brand: ProductBasketCreate, session: AsyncSession = Depends(get_async_session), ):
    stmt = (
        update(ProductsBasket)
        .where(ProductsBasket.id == product_basket_id)
        .values(**brand.dict())
        .returning(ProductsBasket)
    )
    result = await session.execute(stmt)
    updated_product = result.scalar()
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await session.commit()
    return updated_product


@router.delete("/{product_basket_id}", response_model=ProductBasketRead)
async def brand_delete(product_basket_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        update(ProductsBasket)
        .where(ProductsBasket.id == product_basket_id)
        .values({"is_deleted": True})
        .returning(ProductsBasket)
    )
    result = await session.execute(stmt)
    delete_product = result.scalar()
    if delete_product is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await session.commit()
    return delete_product

