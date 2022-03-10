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
        username_field.send_keys("alice1\n")

        # The page refreshes and there is now an error message at the bottom of the form
        #
        error = self.browser.find_element_by_id("form__error")
        self.assertEqual(error.text, "Please insert a valid time")

        # She then correctly inputs her username with a solve time and hits submit.

        # She sees her new username and score in the leaderboard.
        self.fail("Finish the test!")
