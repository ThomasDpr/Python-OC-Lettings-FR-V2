from django.urls import reverse, resolve
from profiles import views


def test_profiles_index_url():
    """Test that profiles index URL resolves correctly."""
    url = reverse("profiles:index")
    assert url == "/profiles/"
    assert resolve(url).func == views.index


def test_profile_detail_url():
    """Test that profile detail URL resolves correctly."""
    url = reverse("profiles:profile", kwargs={"username": "testuser"})
    assert url == "/profiles/testuser/"
    assert resolve(url).func == views.profile
