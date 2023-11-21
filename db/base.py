from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import user_name, host, port, password, db_name


def create_engine_string():
	result = f"postgresql+asyncpg://{user_name}:{password}@{host}:{port}/{db_name}"
	return result


Base = declarative_base()
Session = async_sessionmaker(create_async_engine(create_engine_string()), expire_on_commit=False)


def create_session() -> AsyncSession:
	return Session()