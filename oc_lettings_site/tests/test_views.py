import pytest

pytestmark = pytest.mark.django_db


def test_homepage_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_uses_template(client):
    response = client.get("/")
    # adapte si ton template diffère
    assert any("index" in t.name for t in response.templates if t.name)


def test_homepage_has_links(client):
    response = client.get("/")
    content = response.content.decode()
    assert "Profiles" in content
    assert "Lettings" in content
