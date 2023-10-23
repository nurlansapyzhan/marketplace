from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.basket.schemas.address import AddressRead, AddressCreate

from src.auth.models import address

router = APIRouter(
    prefix="/address",
    tags=["Address"]
)


@router.get("/", response_model=List[AddressRead])
async def get_address_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                           page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                           session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(address).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{address_id}", response_model=AddressRead)
async def get_address_detail(address_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(address).filter_by(id=address_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/")
async def post_address_create(new_address: AddressCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(address).values(**new_address.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{address_id}", response_model=AddressCreate)
async def put_address_update(address_id: int, address: AddressCreate,
                             session: AsyncSession = Depends(get_async_session), ):
    stmt = (
        update(address)
        .where(address.id == address_id)
        .values(**address.dict())
        .returning(address)
    )
    result = await session.execute(stmt)
    updated_address = result.scalar()
    if updated_address is None:
        raise HTTPException(status_code=404, detail="Address not found")

    await session.commit()
    return updated_address


@router.delete("/{address_id}", response_model=AddressRead)
async def address_delete(address_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        update(address)
        .where(address.id == address_id)
        .values({"is_deleted": True})
        .returning(address)
    )
    result = await session.execute(stmt)
    delete_address = result.scalar()
    if delete_address is None:
        raise HTTPException(status_code=404, detail="Address not found")

    await session.commit()
    return delete_address
