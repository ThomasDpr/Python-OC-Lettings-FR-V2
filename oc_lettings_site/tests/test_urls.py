from django.urls import reverse, resolve
from oc_lettings_site import views


def test_homepage_url():
    """Test that homepage URL resolves correctly."""
    url = reverse("index")
    assert url == "/"
    assert resolve(url).func == views.index
