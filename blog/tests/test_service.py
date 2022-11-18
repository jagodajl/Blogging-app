import pytest

from blog import app

TITLE = "Test title"
BODY = "Test body text"
IMG_URL = "Test url"


@pytest.fixture
def test_home():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200


def test_open_new_post_form():
    with app.test_client() as client:
        response_home = client.get("/")
        response_get_post = client.get("/post")

        assert response_home.status_code == 200  # ok
        assert response_get_post.status_code == 308  # dlaczego http status 308? wszystko oprócz home ma 308?
