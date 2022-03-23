from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomepageTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path="D:\\Projects\\NYT Leaderboard Website\\geckodriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_cannot_add_empty_entry_times(self):

        # Alice goes to the home page and starts to fill out an entry.
        self.browser.get(self.live_server_url)

        # She inputs a username but then hits submit with inputting any times.
        username_field = self.browser.find_element_by_id("id_username")
        username_field.send_keys("alice1")

        submit_button = self.browser.find_element_by_id("form__submit")
        submit_button.click()

        # The page refreshes and there is now an error message at the bottom of the form
        #
        error = self.browser.find_element_by_id("form__error")
        self.assertEqual(error.text, "Invalid time")

        # She then inputs her solve time and hits submit.
        hour_field = self.browser.find_element_by_id("id_hours")
        hour_field.clear()
        hour_field.send_keys("0")
        minute_field = self.browser.find_element_by_id("id_minutes")
        minute_field.clear()
        minute_field.send_keys("20")
        second_field = self.browser.find_element_by_id("id_seconds")
        second_field.clear()
        second_field.send_keys("5")

        submit_button = self.browser.find_element_by_id("form__submit")
        submit_button.click()

        # She sees her new username and score in the leaderboard.
        leaderboard = self.browser.find_element_by_id("leaderboard")
        rows = leaderboard.find_elements(by="tag name", value="li")
        self.assertIn("alice1 | 00:20:05", [row.text for row in rows])
