from __future__ import annotations

from typing import AsyncGenerator, Optional

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, UniqueConstraint, Integer


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    speed: Mapped[float] = mapped_column(Float)


class CommandLog(Base):
    __tablename__ = "command_logs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(String(64))
    command_id: Mapped[str] = mapped_column(String(128))
    __table_args__ = (
        UniqueConstraint("session_id", "command_id", name="uix_session_command"),
    )


_engine: Optional[object] = None
_SessionLocal: Optional[async_sessionmaker[AsyncSession]] = None


async def _ensure_engine():
    global _engine, _SessionLocal
    if _engine is None or _SessionLocal is None:
        # Shared in-memory SQLite database (no external DB)
        database_url = "sqlite+aiosqlite:///file:memdb1?mode=memory&cache=shared&uri=true"
        _engine = create_async_engine(database_url, echo=False, connect_args={"uri": True})
        _SessionLocal = async_sessionmaker(_engine, expire_on_commit=False, class_=AsyncSession)
        async with _engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    # Lazily initialize a module-scoped engine/sessionmaker independent of app lifespan
    await _ensure_engine()
    assert _SessionLocal is not None
    async with _SessionLocal() as session:
        yield session
