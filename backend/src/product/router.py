from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session

from src.product.schemas import ProductCreate

from src.product.models import Product

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get("/")
async def get_specific_operations( session: AsyncSession = Depends(get_async_session)):
    query = select(Product)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_specific_operations(new_operation: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Product).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}