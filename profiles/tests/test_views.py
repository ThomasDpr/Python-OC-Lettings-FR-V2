import pytest
from django.contrib.auth.models import User
from profiles.models import Profile

pytestmark = pytest.mark.django_db


@pytest.fixture
def profile():
    user = User.objects.create_user(username="bob", password="pass1234")
    return Profile.objects.create(user=user, favorite_city="Berlin")


def test_profiles_index_status_code(client):
    response = client.get("/profiles/")
    assert response.status_code == 200


def test_profiles_index_lists_user(client, profile):
    response = client.get("/profiles/")
    assert profile.user.username in response.content.decode()


def test_profile_detail_status_code(client, profile):
    response = client.get(f"/profiles/{profile.user.username}/")
    assert response.status_code == 200


def test_profile_detail_shows_favorite_city(client, profile):
    response = client.get(f"/profiles/{profile.user.username}/")
    assert profile.favorite_city in response.content.decode()


def test_profile_detail_404_if_not_found(client):
    response = client.get("/profiles/no_such_user/")
    assert response.status_code == 404
