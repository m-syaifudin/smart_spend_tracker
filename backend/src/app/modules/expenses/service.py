import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.expenses import repository
from app.modules.expenses.schemas import ExpenseCreate
from ...shared.exception import NotFoundException
from ...core.logging import log


async def add_expense(db: AsyncSession, data: ExpenseCreate):
    log.info("expense_create_requested", title=data.title, amount=str(data.amount))
    return await repository.create_expense(db, data)


async def get_expenses(db: AsyncSession):
    return await repository.list_expenses(db)

async def get_expense(db: AsyncSession, expense_id: uuid.UUID):
    expense = await repository.get_by_id(db,expense_id)
    if not expense:
        raise NotFoundException(f"Expense {expense_id} not found")
    return expense