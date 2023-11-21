from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import Manhva


async def get_manhva_names(session: AsyncSession):
	names = await session.execute(select(Manhva.manhva_name).where(Manhva.archived == False))
	names = names.scalars().all()
	return names
