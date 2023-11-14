import pytest
from main import CRUDApp


@pytest.fixture
def app():
    return CRUDApp().app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Items" in response.data.decode()


def test_add_item(client):
    response = client.post("/add", data={"name": "New Item"}, follow_redirects=True)
    assert response.status_code == 200
    assert "New Item" in response.data.decode()


def test_edit_item(client):
    response = client.post(
        "/edit/1", data={"name": "Updated Item"}, follow_redirects=True
    )
    assert response.status_code == 200
    assert "Updated Item" in response.data.decode()


def test_delete_item(client):
    response = client.get("/delete/4", follow_redirects=True)
    assert response.status_code == 200
    assert "Item 1" not in response.data.decode()
