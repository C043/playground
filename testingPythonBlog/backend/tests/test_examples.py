import pytest


@pytest.mark.asyncio
async def test_create_item(client):
    payload = {"title": "Hello", "speed": 1.25}
    resp = await client.post("/items", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "Hello"
    assert "id" in data


@pytest.mark.asyncio
async def test_create_item_invalid_speed(client):
    payload = {"title": "T", "speed": "fast"}
    resp = await client.post("/items", json=payload)
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_items_crud(client):
    # create
    resp = await client.post("/items", json={"title": "A", "speed": 1.0})
    assert resp.status_code == 201
    item = resp.json()

    # list
    resp = await client.get("/items")
    assert resp.status_code == 200
    items = resp.json()
    assert any(x["id"] == item["id"] for x in items)


@pytest.mark.asyncio
async def test_command_idempotent(client):
    cmd = {"command": "pause", "command_id": "abc-123"}
    resp1 = await client.post("/session/42/commands", json=cmd)
    resp2 = await client.post("/session/42/command", json=cmd)
    assert resp1.status_code == 200 and resp2.status_code == 200
    assert resp1.json()["applied"] is True
    assert resp2.json()["applied"] is False


@pytest.mark.asyncio
async def test_protected_requires_auth(client):
    resp = await client.get("/me")
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_protected_with_token(client):
    headers = {"Authorization": "bearer testtoken"}
    resp = await client.get("/me", headers=headers)
    assert resp.status_code == 200
