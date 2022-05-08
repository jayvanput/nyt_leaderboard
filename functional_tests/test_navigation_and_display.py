from time import sleep
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

class PageTests(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = WebDriver(
            executable_path="D:\\Projects\\NYT Leaderboard Website\\geckodriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def input_time(self,username,time_str):
        
        hours, minutes, seconds = time_str.split(":")

        self.browser.find_element_by_id("show_form").click()

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
        self.browser.implicitly_wait(3)

        # Return the updated user & time lists.
        leaderboard = self.browser.find_element_by_id("entries")
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
        header_text = self.browser.find_element_by_tag_name("h2").text
        self.assertIn("Leaderboard", header_text)

        # She sees a leaderboard with today's date that already has some users and times in it.
        header_text = self.browser.find_element_by_tag_name("h4").text
        today_text = datetime.date.today().strftime("%A, %B %d %Y")
        self.assertIn(today_text, header_text)

        # She sees a button to add a new entry.
        button_text = self.browser.find_element_by_id("show_form").text
        self.assertEqual(button_text, "Submit Time")

        # A form appears and she enters a username and time (hours, minutes, seconds).
        users, times = self.input_time("alice1","00:20:05")

        # She can see her time has now been added to the leaderboard.
        self.assertIn("🥇. alice1", users)
        self.assertIn("00:20:05", times)
        # Satisfied with her time today, she closes the site.
    
    def test_leaderboard_shows_proper_order_with_medals(self):
        # Alice goes to input her time for today's leaderboard.
        self.browser.get(self.live_server_url)

        # She notices her friend Bob's time of (00:15:42) is already on the scoreboard.
        self.input_time("Bob2","00:15:42")

        # She also notices her friend Charlie's time of (00:07:08) is also on the scoreboard.
        users, times = self.input_time("Charlie3","00:07:08")
        
        self.assertIn("🥈. Bob2",users)
        self.assertIn("00:15:42",times)
        self.assertIn("🥇. Charlie3",users)
        self.assertIn("00:07:08",times)
        
        # She sees Charlie is first on the leaderboard and Bob is second.
        self.assertEqual("🥇. Charlie3",users[0])
        self.assertEqual("🥈. Bob2",users[1])

        # She inputs her time (00:11:55) for today's puzzle and another time is inserted (00:54:22).
        self.input_time("Alice1","00:11:55")
        new_users, new_times = self.input_time("Debra","00:22:35")
        new_users, new_times = self.input_time("Ezekiel","00:45:36")

        # After inputting her time, she sees that she is now in second and Bob has moved to third.
        self.assertEqual("🥇. Charlie3",new_users[0])
        self.assertEqual("🥈. Alice1",new_users[1])
        self.assertEqual("🥉. Bob2",new_users[2])

        # A new time is added that is slower than all. Alice confirms it does not get a medal.
        self.assertEqual("4. Debra",new_users[3])
        self.assertEqual("00:22:35",new_times[3])


    def test_user_can_navigate_with_buttons(self):

        # Alice goes to the website and is brought to the homepage.
        self.browser.get(self.live_server_url)

        # She wants to check her score from yesterday, so she uses the arrow buttons to go back 1 day.
        yesterday_date = datetime.date.today() - datetime.timedelta(days=1)
        yesterday_date_str = yesterday_date.strftime("%Y/%m/%d")

        self.browser.find_element_by_id("nav__prev").click()
        self.browser.implicitly_wait(3)
        self.assertIn(yesterday_date_str,self.browser.current_url)

        # She also want to see how she did on this day last week, so she uses the date picker to go back.
        last_week_date = datetime.date.today() - datetime.timedelta(days=7)
        last_week_date_str = last_week_date.strftime("%m/%d/%Y")

        date_picker = self.browser.find_element_by_id("nav__date")
        date_picker.send_keys(last_week_date_str)
        submit_btn = self.browser.find_element_by_id("nav__submit")
        submit_btn.click()
        self.browser.implicitly_wait(3)

        self.assertIn("date_picker",self.browser.current_url)
    
        # Satified, she closes the site.
