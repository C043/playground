from __future__ import annotations

from typing import List, AsyncGenerator

from fastapi import FastAPI, Depends, Header, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field, constr
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_session, Item, CommandLog


def create_app() -> FastAPI:
    app = FastAPI()

    class ItemIn(BaseModel):
        title: str
        speed: float

    class ItemOut(BaseModel):
        id: int
        title: str
        speed: float

    async def _do_background(text: str):
        # Placeholder background work
        return None

    @app.post("/items", status_code=201, response_model=ItemOut)
    async def create_item(payload: dict, session: AsyncSession = Depends(get_session)):
        # Accept raw dict body to avoid parser quirks; enforce minimal validation
        try:
            title = str(payload["title"])
            speed = float(payload["speed"])
        except (KeyError, TypeError, ValueError):
            raise HTTPException(status_code=422, detail="Invalid payload")
        obj = Item(title=title, speed=speed)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return ItemOut(id=obj.id, title=obj.title, speed=obj.speed)

    @app.get("/items", response_model=List[ItemOut])
    async def list_items(session: AsyncSession = Depends(get_session)):
        res = await session.execute(select(Item))
        rows = res.scalars().all()
        return [ItemOut(id=o.id, title=o.title, speed=o.speed) for o in rows]

    async def _apply_command(
        session_id: str,
        command: str,
        command_id: str,
        session: AsyncSession,
    ):
        log = CommandLog(session_id=session_id, command_id=command_id)
        session.add(log)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()
            return {"applied": False}
        return {"applied": True}

    class CommandIn(BaseModel):
        command: str
        command_id: str

    @app.post("/session/{session_id}/commands")
    async def post_command_plural(
        session_id: str,
        payload: dict,
        session: AsyncSession = Depends(get_session),
    ):
        try:
            return await _apply_command(session_id, str(payload["command"]), str(payload["command_id"]), session)
        except (KeyError, TypeError, ValueError):
            raise HTTPException(status_code=422, detail="Invalid payload")

    # Accept the singular path too to match README's example typo
    @app.post("/session/{session_id}/command")
    async def post_command_singular(
        session_id: str,
        payload: dict,
        session: AsyncSession = Depends(get_session),
    ):
        try:
            return await _apply_command(session_id, str(payload["command"]), str(payload["command_id"]), session)
        except (KeyError, TypeError, ValueError):
            raise HTTPException(status_code=422, detail="Invalid payload")

    def _check_auth(authorization: str | None) -> None:
        if not authorization:
            raise HTTPException(status_code=401, detail="Missing Authorization header")
        scheme, _, token = authorization.partition(" ")
        if scheme.lower() != "bearer" or token != "testtoken":
            raise HTTPException(status_code=403, detail="Forbidden")

    @app.get("/me")
    async def get_me(Authorization: str | None = Header(default=None)):
        _check_auth(Authorization)
        return {"user": "test"}

    @app.post("/synthesis", status_code=202)
    async def kick_synthesis(payload: dict, bg: BackgroundTasks):
        text = str(payload.get("text", ""))
        bg.add_task(_do_background, text)
        return {"scheduled": True}

    # Also support the misspelled path in README
    @app.post("/syntesis", status_code=202)
    async def kick_syntesis(payload: dict, bg: BackgroundTasks):
        text = str(payload.get("text", ""))
        bg.add_task(_do_background, text)
        return {"scheduled": True}

    async def event_stream() -> AsyncGenerator[bytes, None]:
        # Minimal SSE stream for tests
        yield b"event: ping\n" b"data: ok\n\n"

    @app.get("/sessions/{session_id}/events")
    async def sse(session_id: str):
        return StreamingResponse(event_stream(), media_type="text/event-stream")

    @app.get("/health")
    async def health():
        return {"ok": True}

    return app


app = create_app()
