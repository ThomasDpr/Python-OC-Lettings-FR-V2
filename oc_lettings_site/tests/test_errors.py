import pytest

pytestmark = pytest.mark.django_db


def test_custom_404_page(client):
    response = client.get("/une-url-qui-nexiste-pas/")
    assert response.status_code == 404
    content = response.content.decode().lower()
    assert "404" in content


def test_custom_500_page(client, settings):
    # j'init la variable DEBUG à False pour que le 500 soit bien affiché
    settings.DEBUG = False
    # je dis que le client doit raiser une exception de requête
    client.raise_request_exception = False

    response = client.get("/sentry-debug/")
    # je vérifie que le status code est 500 et que le contenu contient le texte "500"

    assert response.status_code == 500
    assert b"500" in response.content
