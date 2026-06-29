import pytest

pytestmark = pytest.mark.asyncio


async def test_health_check(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


async def test_create_and_get_expense(client):
    payload = {"title": "Lunch", "amount": 15.0, "category": "food"}
    create_resp = await client.post("/expenses/", json=payload)
    assert create_resp.status_code == 201
    expense_id = create_resp.json()["id"]

    get_resp = await client.get(f"/expenses/{expense_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Lunch"