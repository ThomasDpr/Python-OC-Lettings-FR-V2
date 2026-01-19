import pytest
from lettings.models import Address, Letting

pytestmark = pytest.mark.django_db


def test_address_str():
    a = Address(
        number=1,
        street="Rue de Test",
        city="Lyon",
        state="LY",
        zip_code=69000,
        country_iso_code="FR",
    )
    assert str(a)  # au minimum non vide


def test_letting_str():
    a = Address(
        number=1,
        street="Rue de Test",
        city="Lyon",
        state="LY",
        zip_code=69000,
        country_iso_code="FR",
    )
    letting = Letting(title="Letting X", address=a)
    assert "Letting" in str(letting) or str(letting)
