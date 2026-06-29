import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.modules.expenses import service
from app.modules.expenses.schemas import ExpenseCreate, ExpenseRead

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("/", response_model=ExpenseRead, status_code=201)
async def create_expense(data: ExpenseCreate, db: AsyncSession = Depends(get_db)):
    return await service.add_expense(db, data)


@router.get("/", response_model=list[ExpenseRead])
async def list_expenses(db: AsyncSession = Depends(get_db)):
    return await service.get_expenses(db)

@router.get("/{expense_id}", response_model=ExpenseRead)
async def get_expense(expense_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await service.get_expense(db, expense_id)

