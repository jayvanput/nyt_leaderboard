from asyncio import exceptions
from cmath import exp
from multiprocessing.connection import wait
from time import sleep
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
        button_text = self.browser.find_element_by_id("show_form").text
        self.assertEqual(button_text, "Submit Time")

        # A form appears and she enters a username and time (hours, minutes, seconds).
        username_field = self.browser.find_element_by_id("username")
        username_field.send_keys("alice1")
        hour_field = self.browser.find_element_by_id("hours")
        hour_field.send_keys("0")
        minute_field = self.browser.find_element_by_id("minutes")
        minute_field.send_keys("20")
        second_field = self.browser.find_element_by_id("seconds")
        second_field.send_keys("5\n")

        # She clicks on the submit button and is redirected back to the page.

        # She can see her time has now been added to the leaderboard.
        leaderboard = self.browser.find_element_by_id("leaderboard")
        rows = leaderboard.find_elements_by_tag_name("li")
        self.assertIn("alice1 | 00:20:05", [row.text for row in rows])

        # Satisfied with her time today, she closes the site.
