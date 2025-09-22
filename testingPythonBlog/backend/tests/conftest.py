import asyncio
import os
import sys
import pytest
import httpx

# Ensure the backend/ directory (which contains the 'app' package) is on sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app.main import create_app


@pytest.fixture
async def app():
    # Simply create the app; httpx transport will manage lifespan
    return create_app()


@pytest.fixture
async def client(app):
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
