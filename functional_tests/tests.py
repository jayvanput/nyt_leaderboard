from django.test import LiveServerTestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from datetime import date


class HomepageTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_input_new_entry_to_leaderboard(self):
        # Alice learns about a new NYT leaderboard app and checks it out.
        self.browser.get(self.live_server_url)

        # She notices the page title mentions the leaderboard.
        self.assertIn("NYTimes Crossword Leaderboard", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Leaderboard", header_text)

        # She sees a leaderboard with today's date that already has some users and times in it.
        header_text = self.browser.find_element_by_tag_name("h2").text
        today_text = date.today().strftime("%A, %B %d %Y")
        self.assertIn(today_text, header_text)

        # She sees a button to add a new entry.

        # A box appears that asks for a username (text)

        # The box also contains 3 time dropdowns for hours, minutes, and seconds.

        # She clicks on the submit button and is redirected back to the page.

        # She can see her time has now been added to the leaderboard.

        # Satisfied with her time today, she closes the site.
        self.fail("finish the test")
