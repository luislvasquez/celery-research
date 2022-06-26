import os
from typing import Generator
from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from contextlib import contextmanager, asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")


# SYNC ENGINE INITIALIZATION
SQLALCHEMY_SYNC_DB_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(
    SQLALCHEMY_SYNC_DB_URI,
    pool_pre_ping=True,
    pool_size=4, 
    max_overflow=6
)

SessionLocal = sessionmaker(autocommit=False, expire_on_commit=False, autoflush=False, bind=engine)

@contextmanager
def db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ASYNC ENGINE INITIALIZATION
SQLALCHEMY_ASYNC_DB_URI = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
async_engine = create_async_engine(
    SQLALCHEMY_ASYNC_DB_URI,
    pool_pre_ping=True,
    pool_size=4, 
    max_overflow=6,
)

AsyncSessionLocal = sessionmaker(autocommit=False, expire_on_commit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

@asynccontextmanager
async def async_db_session() -> Generator[AsyncSession, None, None]:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()
