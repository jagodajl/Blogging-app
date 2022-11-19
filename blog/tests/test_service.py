import pytest

from blog import app

TITLE = "Test title"
BODY = "Test body text"
IMG_URL = "Test url"


@pytest.fixture
def fixture():
    pass


def test_open_new_post_form():
    with app.test_client() as client:
        response_get_post = client.get("/post/")
        assert response_get_post.status_code == 302
