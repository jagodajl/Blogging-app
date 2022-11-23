import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BLOG_URL = 'http://127.0.0.1:5000'


@pytest.fixture()
def chrome_web_driver():
    return webdriver.Chrome('blog/tests/web_drivers/')  # using chrome for macOs intell


# Blog integration testing
def test_open_home_blog_page(chrome_web_driver):
    with chrome_web_driver:
        chrome_web_driver.get(BLOG_URL)
        time.sleep(5)
        expected_search = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/p')
        assert expected_search.text == str("Life is short, and the world is wide...")
        time.sleep(5)
        chrome_web_driver.quit()


def test_check_weather(chrome_web_driver):
    with chrome_web_driver:
        chrome_web_driver.get(BLOG_URL)
        time.sleep(5)
        weather_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[1]/a')
        weather_button.click()
        time.sleep(1)
        assert chrome_web_driver.current_url == 'https://weather.com/?Goto=Redirected'
        time.sleep(5)
        chrome_web_driver.quit()


def test_log_in_and_out_blog_page(chrome_web_driver):
    with chrome_web_driver:
        chrome_web_driver.get(BLOG_URL)
        time.sleep(5)

        # LogIn
        login_in_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[3]/a')
        login_in_button.click()
        time.sleep(2)
        user_name_box = chrome_web_driver.find_element(By.NAME, 'username')
        user_name_box.send_keys('admin')
        password_box = chrome_web_driver.find_element(By.NAME, 'password')
        password_box.send_keys('admin')
        time.sleep(2)
        login_in_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/button')
        login_in_button.click()
        logged_blog = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[5]/form/button')
        assert logged_blog.text == str('Logout')
        expected_log_in_message = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/ul/p')
        assert expected_log_in_message.text == str('You are now logged in.')
        time.sleep(3)

        # LogOut
        log_out_button = chrome_web_driver.find_element(
            By.XPATH,
            '/html/body/div/div[1]/nav/div/div/ul/li[5]/form/button'
        )
        log_out_button.click()
        expected_log_out_message = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/ul/p')
        assert expected_log_out_message.text == str('You are now logged out.')
        time.sleep(5)
        chrome_web_driver.quit()


def test_add_edit_and_delete_draft_post(chrome_web_driver):
    with chrome_web_driver:
        chrome_web_driver.get(BLOG_URL)
        time.sleep(5)
        # Log in
        login_in_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[3]/a')
        login_in_button.click()
        time.sleep(2)
        user_name_box = chrome_web_driver.find_element(By.NAME, 'username')
        user_name_box.send_keys('admin')
        password_box = chrome_web_driver.find_element(By.NAME, 'password')
        password_box.send_keys('admin')
        time.sleep(2)
        login_in_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/button')
        login_in_button.click()
        time.sleep(3)
        # Create draft post
        add_new_post_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a')
        add_new_post_button.click()
        time.sleep(2)
        post_title_box = chrome_web_driver.find_element(By.NAME, 'title')
        post_title_box.send_keys("Malbork")
        post_body_box = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div[3]/div[3]')
        post_body_box.send_keys("Malbork castle")
        post_img_url_box = chrome_web_driver.find_element(By.NAME, 'post_img')
        post_img_url_box.send_keys("https://cdn.getyourguide.com/img/location/5962171172ec7.jpeg/99.jpg")
        time.sleep(2)
        post_save_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/button')
        post_save_button.click()
        expected_created_post_message = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/ul/p')
        assert expected_created_post_message.text == str('Post created and saved in Drafts')
        time.sleep(3)

        # Go to drafts
        drafts_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[3]/a')
        drafts_button.click()
        expected_search = chrome_web_driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr/td[2]")
        assert expected_search.text == "Malbork"
        time.sleep(5)

        # Edit draft post
        edit_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr/td[4]/a[1]')
        edit_button.click()
        time.sleep(3)
        post_title_box = chrome_web_driver.find_element(By.NAME, 'title')
        post_title_box.clear()
        time.sleep(3)
        post_title_box.send_keys("Malbork, Poland")
        time.sleep(2)
        post_save_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/button')
        post_save_button.click()
        time.sleep(2)
        expected_edit_message = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/ul/p')
        assert expected_edit_message.text == str('Your Post has been updated!')
        time.sleep(3)

        # Go to edited draft
        drafts_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[3]/a')
        drafts_button.click()
        expected_search = chrome_web_driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr/td[2]")
        assert expected_search.text == "Malbork, Poland"
        time.sleep(5)

        # Delete edited draft
        delete_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr/td[4]/a[2]')
        delete_button.click()
        expected_deletion = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/ul/p')
        assert expected_deletion.text == str('Post Deleted.')
        time.sleep(5)
        chrome_web_driver.quit()


def test_add_and_publish_new_post(chrome_web_driver):
    with chrome_web_driver:
        chrome_web_driver.get(BLOG_URL)
        time.sleep(5)
        # Log in
        login_in_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[3]/a')
        login_in_button.click()
        time.sleep(2)
        user_name_box = chrome_web_driver.find_element(By.NAME, 'username')
        user_name_box.send_keys('admin')
        password_box = chrome_web_driver.find_element(By.NAME, 'password')
        password_box.send_keys('admin')
        time.sleep(2)
        login_in_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/button')
        login_in_button.click()

        # Create published post
        add_new_post_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a')
        add_new_post_button.click()
        time.sleep(2)
        post_title_box = chrome_web_driver.find_element(By.NAME, 'title')
        post_title_box.send_keys("Malbork, Poland")
        post_body_box = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div[3]/div[3]')
        post_body_box.send_keys("Malbork castle")
        post_img_url_box = chrome_web_driver.find_element(By.NAME, 'post_img')
        post_img_url_box.send_keys("https://cdn.getyourguide.com/img/location/5962171172ec7.jpeg/99.jpg")
        post_make_to_publish = chrome_web_driver.find_element(By.NAME, 'is_published')
        post_make_to_publish.click()
        time.sleep(2)
        post_save_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/button')
        post_save_button.click()
        time.sleep(2)
        expected_added_post = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/h2')
        assert expected_added_post.text == 'Malbork, Poland'
        expected_created_new_post_message = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/ul/p')
        assert expected_created_new_post_message.text == str('Your Post has been published!')
        time.sleep(5)
        chrome_web_driver.quit()


def test_contact_messaging(chrome_web_driver):
    with chrome_web_driver:
        chrome_web_driver.get(BLOG_URL)
        time.sleep(5)

        # Contact
        contact_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a')
        contact_button.click()
        time.sleep(2)
        email_box = chrome_web_driver.find_element(By.NAME, 'email')
        email_box.send_keys('jagoda.jeczmien@gmail.com')
        name_box = chrome_web_driver.find_element(By.NAME, 'name')
        name_box.send_keys('Jagoda')
        surname_box = chrome_web_driver.find_element(By.NAME, 'surname')
        surname_box.send_keys('Jeczmien-Lazur')
        title_box = chrome_web_driver.find_element(By.NAME, 'title')
        title_box.send_keys('Have fun')
        content_box = chrome_web_driver.find_element(By.NAME, 'email_content')
        content_box.send_keys('Let\'s have fun')
        time.sleep(2)
        send_email_button = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/button')
        send_email_button.click()
        expected_sent_message = chrome_web_driver.find_element(By.XPATH, '/html/body/div/div[2]/ul/p')
        assert expected_sent_message.text == str('Your email has been sent!')
        time.sleep(5)
        chrome_web_driver.quit()
