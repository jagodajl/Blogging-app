from datetime import date

import pytest

from blog import app


@pytest.fixture
def app_client():
    app.config['WTF_CSRF_ENABLED'] = False
    return app.test_client()


@pytest.fixture
def today_date():
    return date.today()


def test_home_page(app_client):
    with app_client:
        expected_html_cut_off = "Life is short, and the world is wide..."
        response_home = app_client.get("/")
        assert response_home.status_code == 200
        html = str(response_home.get_data())
        count = html.count(expected_html_cut_off)
        assert count == 1


def test_open_new_login_form(app_client):
    with app_client:
        expected_html_cut_off = "Login Page"
        response_get_login_form = app_client.get("/login/")
        assert response_get_login_form.status_code == 200
        html = str(response_get_login_form.get_data())
        count = html.count(expected_html_cut_off)
        assert count == 1


def test_login(app_client):
    with app_client:
        form_data = {
            'username': 'admin',
            'password': 'admin',
        }
        response_login = app_client.post("/login/", data=form_data, follow_redirects=True)
        assert response_login.status_code == 200


def test_logout(app_client):
    with app_client:
        response_logout = app_client.post("/logout/", follow_redirects=True)
        assert response_logout.status_code == 200


def test_open_new_post_form(app_client):
    with app_client as ac:
        with ac.session_transaction() as sess:
            sess["logged_in"] = True
        expected_html_cut_off = "Add new post"
        response_get_post_form = app_client.get("/post/")
        assert response_get_post_form.status_code == 200
        html = str(response_get_post_form.get_data())
        count = html.count(expected_html_cut_off)
        assert count == 1


def test_create_new_post(app_client):
    with app_client as ac:
        with ac.session_transaction() as sess:
            sess["logged_in"] = True
        form_data = {
            'title': 'Title',
            'body': 'Content',
            'post_img': 'Image url'
        }
        response_create_post = app_client.post("/post/", data=form_data, follow_redirects=True)
        assert response_create_post.status_code == 200


def test_open_edit_post_form(app_client, monkeypatch):
    with app_client as ac:
        with ac.session_transaction() as sess:
            sess["logged_in"] = True
        existing_edit_id = 7
        expected_html_cut_off = "Add new post"
        expected_img_utl_for_edit = "https://www.miavolta.com/wp-content/uploads/2022/02/Pula-6.jpg"
        # mocked_post_entry = Entry(id=1, title="Title", body="Body", post_img="post_img", pub_date=today_date)
        # monkeypatch.setattr(service, 'get_entry_by_id', lambda mock: mocked_post_entry)
        response_get_form_edit_post = app_client.get(f"/edit-post/{existing_edit_id}", follow_redirects=False)
        assert response_get_form_edit_post.status_code == 200
        html = str(response_get_form_edit_post.get_data())
        count = html.count(expected_html_cut_off)
        count_img_url = html.count(expected_img_utl_for_edit)
        assert count == 1
        assert count_img_url == 1


def test_edit_post(app_client, monkeypatch):
    with app_client as ac:
        with ac.session_transaction() as sess:
            sess["logged_in"] = True
        edit_id = 3
        # mocked_post_entry = Entry(id=1, title="Title", body="Body", post_img="dupa", pub_date=today_date)
        # monkeypatch.setattr(service, 'get_entry_by_id', lambda mock: mocked_post_entry)
        response_get_form_edit_post = app_client.post(f"/edit-post/{edit_id}", follow_redirects=True)
        assert response_get_form_edit_post.status_code == 200


def test_open_show_drafts_form(app_client):
    with app_client:
        expected_html_cut_off = "My Drafts"
        response_get_form_show_drafts = app_client.get("/drafts/")
        assert response_get_form_show_drafts.status_code == 200
        html = str(response_get_form_show_drafts.get_data())
        count = html.count(expected_html_cut_off)
        assert count == 1


def test_delete_draft_non_existing(app_client):
    with app_client:
        delete_non_existing_id = -1
        response_get_form_show_drafts = app_client.get(f"/delete/{delete_non_existing_id}")
        assert response_get_form_show_drafts.status_code == 404


def test_delete_draft_existing(app_client):
    with app_client:
        delete_existing_id = 8
        response_get_form_show_drafts = app_client.get(f"/delete/{delete_existing_id}", follow_redirects=True)
        assert response_get_form_show_drafts.status_code == 200


def test_open_contact_form(app_client):
    with app_client:
        expected_html_cut_off = "Get in Touch"
        response_get_login_form = app_client.get("/contact/")
        assert response_get_login_form.status_code == 200
        html = str(response_get_login_form.get_data())
        count = html.count(expected_html_cut_off)
        assert count == 1


def test_contact(app_client):
    with app_client:
        expected_html_cut_off = "Your email has been sent!"
        response_get_login_form = app_client.post("/contact/", follow_redirects=True)
        assert response_get_login_form.status_code == 200
        html = str(response_get_login_form.get_data())
        count = html.count(expected_html_cut_off)
        assert count == 1


def test_about_page(app_client):
    with app_client:
        expected_html_cut_off = "HELLO FELLOW TRAVELERS!"
        response_about = app_client.get("/about/")
        assert response_about.status_code == 200
        html = str(response_about.get_data())
        count = html.count(expected_html_cut_off)
        assert count == 1
