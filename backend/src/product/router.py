from typing import List
import shutil
from fastapi import UploadFile
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.product.schemas import ProductCreate

from src.product.models import Product

from src.product.schemas import ProductRead

from src.product.models import Photo

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get("/", response_model=List[ProductRead])
async def get_specific_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/")
async def add_specific_operations(new_operation: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Product).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/uploadphoto/")
async def upload_photo(file: UploadFile, product_id: int, session: AsyncSession = Depends(get_async_session)):
    with open(f'src/upload/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    stmt = insert(Photo).values({
        'product_id': product_id,
        'url': f'src/upload/{file.filename}'
    })
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
