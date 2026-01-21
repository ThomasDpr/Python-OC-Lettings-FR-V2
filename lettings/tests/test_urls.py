from django.urls import reverse, resolve
from lettings import views


def test_lettings_index_url():
    """Test that lettings index URL resolves correctly."""
    url = reverse("lettings:index")
    assert url == "/lettings/"
    assert resolve(url).func == views.index


def test_letting_detail_url():
    """Test that letting detail URL resolves correctly."""
    url = reverse("lettings:letting", kwargs={"letting_id": 1})
    assert url == "/lettings/1/"
    assert resolve(url).func == views.letting
