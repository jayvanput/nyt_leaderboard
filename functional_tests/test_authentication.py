import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
from dotenv import load_dotenv
from django.contrib.auth.models import User

class AuthenticationTest(StaticLiveServerTestCase):

    username = "testuser"
    password = os.getenv("TEST_USER_PWORD")

    def setUp(self):
        load_dotenv()

        user = User.objects.create_user(username=self.username, password=self.password)
        user.save()

        self.browser = webdriver.Firefox(
            executable_path="D:\\Projects\\NYT Leaderboard Website\\geckodriver.exe")
        self.browser.implicitly_wait(3)



    def tearDown(self):
        self.browser.quit()

    def test_user_can_login_and_input_time(self):

        # Alice goes to the site where she isn't authenticated.
        self.browser.get(self.live_server_url)

        # She clicks the login and is sent to the authentication page. She enters her username and password.
        login_btn = self.browser.find_element_by_id("login_href")
        login_btn.click()
        self.browser.implicitly_wait(3)
        
        self.assertIn("/accounts/login",self.browser.current_url)

        username_field = self.browser.find_element_by_id("id_username")
        username_field.clear()
        username_field.send_keys(self.username)

        password_field = self.browser.find_element_by_id("id_password")
        password_field.clear()
        password_field.send_keys(self.password)

        submit_btn = self.browser.find_element_by_id("id_submit")
        submit_btn.click()
        self.browser.implicitly_wait(3)

        # She is redirected to her homepage where she sees the login button replaced with her username.
        login_btn = self.browser.find_element_by_id("login_href")
        self.assertEqual(login_btn.text, self.username)

        # She goes to enter a time and the username field is already populated with her's.
        modal_btn = self.browser.find_element_by_id("show_form")
        modal_btn.click()
        self.browser.implicitly_wait(3)

        new_username_field = self.browser.find_element_by_name("username")
        self.assertEqual(new_username_field.get_attribute("value"), self.username)

        # She logs out.