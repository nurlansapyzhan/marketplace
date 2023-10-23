from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, Query
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.product.schemas import ProductListRead, ProductRead, ProductCreate, ProductPut, ProductPhoto, ProductPhotoCreate
from src.product.models import Product, Photo
from src.database import get_async_session
import shutil

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.get("/", response_model=List[ProductListRead])
async def get_product_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                           page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                           session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Product).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{product_id}", response_model=ProductRead)
async def get_product_detail(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Product).filter_by(id=product_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/")
async def post_product_create(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{product_id}", response_model=ProductPut)
async def put_product_update(product_id: int, product: ProductPut,
                             session: AsyncSession = Depends(get_async_session), ):
    stmt = (
        update(Product)
        .where(Product.id == product_id)
        .values(**product.dict())
        .returning(Product)
    )
    result = await session.execute(stmt)
    updated_product = result.scalar()
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await session.commit()
    return updated_product


@router.delete("/{product_id}", response_model=ProductRead)
async def product_delete(product_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        update(Product)
        .where(Product.id == product_id)
        .values({"is_deleted": True})
        .returning(Product)
    )
    result = await session.execute(stmt)
    delete_product = result.scalar()
    if delete_product is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await session.commit()
    return delete_product


@router.get("/products_with_photos/", response_model=List[ProductPhoto])
async def get_products_with_photos(session: AsyncSession = Depends(get_async_session)):
    query = (
        select(Product, Photo)
        .join(Product, Product.id == Photo.product_id)
    )
    result = await session.execute(query)
    rows = result.all()
    products_with_photos = {}
    for product, photo in rows:
        if product.id not in products_with_photos:
            product_dict = product.__dict__
            product_dict['photo'] = []
            products_with_photos[product.id] = product_dict
        if photo:
            products_with_photos[product.id]['photo'].append(photo.__dict__)
    products_with_photos_list = [ProductPhoto(**product) for product in products_with_photos.values()]

    return products_with_photos_list


@router.get("/product_with_photos/{product_id}", response_model=ProductPhoto)
async def get_product_with_photos(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = (
        select(Product, Photo)
        .join(Product, Product.id == Photo.product_id)
        .filter(Product.id == product_id)
    )
    result = await session.execute(query)
    rows = result.all()
    products_with_photos = {}
    for product, photo in rows:
        if product.id not in products_with_photos:
            product_dict = product.__dict__
            product_dict['photo'] = []
            products_with_photos[product.id] = product_dict
        if photo:
            products_with_photos[product.id]['photo'].append(photo.__dict__)

    if product_id not in products_with_photos:
        raise HTTPException(status_code=404, detail="Product not found")

    product_with_photos = ProductPhoto(**products_with_photos[product_id])

    return product_with_photos


# @router.post("/create_product_with_photos/", response_model=ProductPhotoCreate)
# async def create_product_with_photos(file_list: List[UploadFile], product_data: ProductPhotoCreate,
#                                      session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(Product).values(**product_data.dict())
#     result = await session.execute(stmt)
#     await session.commit()
#     new_product = result.scalar().first()
#
#     # Создание новых фотографий и связывание их с продуктом
#     photos = []
#     for file in file_list:
#         with open(f'src/upload/{file.filename}', 'wb') as buffer:
#             shutil.copyfileobj(file.file, buffer)
#         new_photo = Photo(
#             product_id=new_product.id,
#             url=f'src/upload/{file.filename}'
#         )
#         session.add(new_photo)
#         photos.append(new_photo)
#
#     await session.commit()
#
#     # Возвращение созданного продукта
#     return new_product


