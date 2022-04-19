from asyncio import exceptions
from cmath import exp
from multiprocessing.connection import wait
from time import sleep
from django.test import LiveServerTestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from datetime import date


class PageTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path="D:\\Projects\\NYT Leaderboard Website\\geckodriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def input_time(self,username,time_str):
        
        hours, minutes, seconds = time_str.split(":")

        username_field = self.browser.find_element_by_id("id_username")
        username_field.send_keys(username)
        hour_field = self.browser.find_element_by_id("id_hours")
        hour_field.clear()
        hour_field.send_keys(hours)
        minute_field = self.browser.find_element_by_id("id_minutes")
        minute_field.clear()
        minute_field.send_keys(minutes)
        second_field = self.browser.find_element_by_id("id_seconds")
        second_field.clear()
        second_field.send_keys(seconds)

        # POST form
        submit_btn = self.browser.find_element_by_id("form__submit")
        submit_btn.click()

        # Return the updated user & time lists.
        leaderboard = self.browser.find_element_by_id("leaderboard")
        users = leaderboard.find_elements(by=By.CLASS_NAME,value="entry_item__user")
        times = leaderboard.find_elements(by=By.CLASS_NAME,value="entry_item__time")
        users = [user.text for user in users]
        times = [time.text for time in times]
        return users, times


    def test_can_input_new_entry(self):
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
        users, times = self.input_time("alice1","00:20:05")

        # She can see her time has now been added to the leaderboard.
        self.assertIn("alice1", users)
        self.assertIn("00:20:05", times)
        # Satisfied with her time today, she closes the site.
        
    
    def test_leaderboard_shows_proper_order(self):
        # Alice goes to input her time for today's leaderboard.
        self.browser.get(self.live_server_url)

        # She notices her friend Bob's time of (00:15:42) is already on the scoreboard.
        self.input_time("Bob2","00:15:42")

        # She also notices her friend Charlie's time of (00:07:08) is also on the scoreboard.
        users, times = self.input_time("Charlie3","00:07:08")
        
        self.assertIn("Bob2",users)
        self.assertIn("00:15:42",times)
        self.assertIn("Charlie3",users)
        self.assertIn("00:07:08",times)
        
        # She sees Charlie is first on the leaderboard and Bob is second.
        self.assertEqual("Charlie3",users[0])
        self.assertEqual("Bob2",users[1])

        # She inputs her time (00:11:55) for today's puzzle.
        new_users, new_times = self.input_time("Alice1","00:11:55")
        self.browser.implicitly_wait(3)

        # After inputting her time, she sees that she is now in second and Bob has moved to third.
        self.assertEqual("Charlie3",new_users[0])
        self.assertEqual("Alice1",new_users[1])
        self.assertEqual("Bob2",new_users[2])

        # Satisfied with time, she closes the site.
