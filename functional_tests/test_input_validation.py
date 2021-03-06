from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ValidationTests(StaticLiveServerTestCase):

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
        modal_btn = self.browser.find_element_by_id("show_form")
        modal_btn.click()

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
        leaderboard = self.browser.find_element_by_id("entries")
        users = leaderboard.find_elements(by=By.CLASS_NAME,value="entry_item__user")
        times = leaderboard.find_elements(by=By.CLASS_NAME,value="entry_item__time")
        self.assertIn("????. alice1", [user.text for user in users])
        self.assertIn("00:20:05", [time.text for time in times])
