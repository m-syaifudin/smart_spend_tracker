import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.expenses.models import Expense
from app.modules.expenses.schemas import ExpenseCreate


async def create_expense(db: AsyncSession, data: ExpenseCreate) -> Expense:
    expense = Expense(**data.model_dump())
    db.add(expense)
    await db.commit()
    await db.refresh(expense)
    return expense


async def list_expenses(db: AsyncSession) -> list[Expense]:
    result = await db.execute(select(Expense).order_by(Expense.created_at.desc()))
    return list(result.scalars().all())

async def get_by_id(db: AsyncSession, expense_id: uuid.UUID) -> Expense | None:
    return await db.get(Expense, expense_id)