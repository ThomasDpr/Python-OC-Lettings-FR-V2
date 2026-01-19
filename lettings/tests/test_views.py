import pytest
from lettings.models import Letting, Address

pytestmark = pytest.mark.django_db


@pytest.fixture
def letting():
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Paris",
        state="TX",
        zip_code=75000,
        country_iso_code="FR",
    )
    return Letting.objects.create(title="Test Letting", address=address)


def test_lettings_index_status_code(client):
    # adapte le reverse si ton url name diffère
    response = client.get("/lettings/")
    assert response.status_code == 200


def test_lettings_index_displays_letting(client, letting):
    response = client.get("/lettings/")
    content = response.content.decode()
    assert letting.title in content


def test_letting_detail_status_code(client, letting):
    response = client.get(f"/lettings/{letting.id}/")
    assert response.status_code == 200


def test_letting_detail_shows_address(client, letting):
    response = client.get(f"/lettings/{letting.id}/")
    content = response.content.decode()
    assert letting.title in content
    assert letting.address.city in content


def test_letting_detail_404_if_not_found(client):
    response = client.get("/lettings/999999/")
    assert response.status_code == 404
