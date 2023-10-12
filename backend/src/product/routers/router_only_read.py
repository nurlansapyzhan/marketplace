from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.product.schemas import ColorRead, CategoryRead, CompoundRead, CollectionRead, SizeRead, SizeLetterRead, \
    SizeNumberRead, PatternRead, ProductSalesTypeRead, ProductCategoryRead, AffiliationRead, SeasonRead
from src.product.models import Color, Compound, Pattern, Season, Collection, Affiliation, Category, ProductCategory, \
    ProductSalesType, SizeNumber, SizeLetter, Size
from src.database import get_async_session

router = APIRouter(
    prefix="/router/read_product",
    tags=["RouterReadProduct"]
)


@router.get("/color", response_model=List[ColorRead])
async def get_color_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                         page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                         session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Color).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/color/{color_id}", response_model=ColorRead)
async def get_color_detail(color_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Color).filter_by(id=color_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/category", response_model=List[CategoryRead])
async def get_category_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                            page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                            session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Category).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/category/{category_id}", response_model=CategoryRead)
async def get_category_detail(category_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Category).filter_by(id=category_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/compound", response_model=List[CompoundRead])
async def get_compound_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                            page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                            session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Compound).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/compound/{compound_id}", response_model=CompoundRead)
async def get_compound_detail(compound_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Compound).filter_by(id=compound_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/collection", response_model=List[CollectionRead])
async def get_collection_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                              page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                              session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Collection).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/collection/{collection_id}", response_model=CollectionRead)
async def get_collection_detail(collection_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Collection).filter_by(id=collection_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/size", response_model=List[SizeRead])
async def get_size_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                        page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                        session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Size).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/size/{size_id}", response_model=SizeRead)
async def get_size_detail(size_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Size).filter_by(id=size_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/size_letter", response_model=List[SizeLetterRead])
async def get_size_letter_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                               page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                               session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(SizeLetter).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/size_letter/{size_letter_id}", response_model=SizeLetterRead)
async def get_size_letter_detail(size_letter_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(SizeLetter).filter_by(id=size_letter_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/size_number", response_model=List[SizeNumberRead])
async def get_size_number_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                               page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                               session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(SizeNumber).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/size_number/{size_number_id}", response_model=SizeNumberRead)
async def get_size_number_detail(size_number: int, session: AsyncSession = Depends(get_async_session)):
    query = select(SizeNumber).filter_by(id=size_number)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/pattern", response_model=List[PatternRead])
async def get_pattern_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                           page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                           session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Pattern).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/pattern/{pattern_id}", response_model=PatternRead)
async def get_pattern_detail(pattern_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Pattern).filter_by(id=pattern_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/product_sales", response_model=List[ProductSalesTypeRead])
async def get_product_sales_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                                 page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                                 session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(ProductSalesType).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/product_sales/{product_sales_id}", response_model=ProductSalesTypeRead)
async def get_product_sales_detail(product_sales_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(ProductSalesType).filter_by(id=product_sales_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/product_category", response_model=List[ProductCategoryRead])
async def get_product_category_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                                    page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                                    session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(ProductCategory).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/product_category/{product_category_id}", response_model=ProductCategoryRead)
async def get_product_category_detail(product_category_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(ProductCategory).filter_by(id=product_category_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/affiliation", response_model=List[AffiliationRead])
async def get_affiliation_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                               page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                               session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Affiliation).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/affiliation/{affiliation_id}", response_model=AffiliationRead)
async def get_affiliation_detail(affiliation_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Affiliation).filter_by(id=affiliation_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.get("/season", response_model=List[SeasonRead])
async def get_season_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                          page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                          session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Season).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/season/{season_id}", response_model=SeasonRead)
async def get_season_detail(season_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Season).filter_by(id=season_id)
    result = await session.execute(query)
    return result.scalars().first()
