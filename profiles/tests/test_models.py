import pytest
from django.contrib.auth.models import User
from profiles.models import Profile

pytestmark = pytest.mark.django_db


def test_profile_str():
    user = User(username="alice")
    p = Profile(user=user, favorite_city="Nice")
    assert "alice" in str(p) or str(p)
