from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.basket.models import Check
from src.basket.schemas import CheckRead, CheckCreate

router = APIRouter(
    prefix="/check",
    tags=["Check"]
)


@router.get("/", response_model=List[CheckRead])
async def get_checks_list(page: Optional[int] = Query(1, description="Номер страницы", ge=1),
                          page_size: Optional[int] = Query(10, description="Размер страницы", ge=1, le=100),
                          session: AsyncSession = Depends(get_async_session)):
    offset = (page - 1) * page_size
    query = select(Check).offset(offset).limit(page_size)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{check_id}", response_model=CheckRead)
async def get_check_detail(check_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Check).filter_by(id=check_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/")
async def post_ckeck_create(new_check: CheckCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Check).values(**new_check.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{check_id}", response_model=CheckCreate)
async def put_check_update(check_id: int, address: CheckCreate,
                           session: AsyncSession = Depends(get_async_session), ):
    stmt = (
        update(Check)
        .where(Check.id == check_id)
        .values(**address.dict())
        .returning(Check)
    )
    result = await session.execute(stmt)
    updated_check = result.scalar()
    if updated_check is None:
        raise HTTPException(status_code=404, detail="Check not found")

    await session.commit()
    return updated_check


@router.delete("/{check_id}", response_model=CheckRead)
async def check_delete(check_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = (
        update(Check)
        .where(Check.id == check_id)
        .values({"is_deleted": True})
        .returning(Check)
    )
    result = await session.execute(stmt)
    delete_check = result.scalar()
    if delete_check is None:
        raise HTTPException(status_code=404, detail="Check not found")

    await session.commit()
    return delete_check
