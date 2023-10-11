from typing import List, Optional
import shutil
from fastapi import APIRouter, Depends, HTTPException, UploadFile, Query
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.product.models import Photo
from src.database import get_async_session
from src.product.schemas import PhotoRead, PhotoCreate

router = APIRouter(
    prefix="/photo",
    tags=["Photo"]
)


@router.get("/", response_model=List[PhotoRead])
async def get_photo_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                         page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                         session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Photo).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{photo_id}", response_model=PhotoRead)
async def get_photo_detail(photo_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Photo).filter_by(id=photo_id)
    result = await session.execute(query)
    return result.scalars().first()


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


@router.put("/updatephoto/{photo_id}")
async def update_photo(photo_id: int, file: UploadFile, session: AsyncSession = Depends(get_async_session)):
    existing_photo = await session.get(Photo, photo_id)
    if existing_photo is None:
        raise HTTPException(status_code=404, detail="Photo not found")
    with open(f'src/upload/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    stmt = (
        update(Photo)
        .where(Photo.id == photo_id)
        .values(url=f'src/upload/{file.filename}')
        .returning(Photo)
    )
    result = await session.execute(stmt)
    updated_photo = result.scalar()
    await session.commit()
    return {"status": "success", "updated_photo": updated_photo}


@router.delete("/{photo_id}", response_model=PhotoRead)
async def get_specific_operations(photo_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        delete(Photo)
        .where(Photo.id == photo_id)
        .returning(Photo)
    )
    result = await session.execute(stmt)
    deleted_product = result.scalar()

    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    await session.commit()
    return deleted_product
#
