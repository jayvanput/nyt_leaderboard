from django.test import TestCase
from django.urls import resolve, reverse
from django.http import HttpRequest
from django.template.loader import render_to_string

from leaderboard.views import home_page, past_leaderboards

import re
import datetime
# Create your tests here.


class ViewTest(TestCase):

    @staticmethod
    def remove_csrf(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_code)

    def assertEqualExceptCSRF(self, html_code1, html_code2):
        return self.assertEqual(
            self.remove_csrf(html_code1),
            self.remove_csrf(html_code2)
        )

    def test_root_url_resolves_to_home_page_view(self):
        home_view = resolve("/")
        self.assertEqual(home_view.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_POST_redirects_to_current_page(self):
        response = self.client.post(
            "/", data={"username": "alice", "hours": "0", "minutes": "10", "seconds": "5"})
        self.assertRedirects(response, "/")

    def test_other_date_uses_correct_template(self):
        response=self.client.get("/2022/04/18")
        self.assertTemplateUsed(response, "past.html")

    def test_todays_date_redirects_to_homepage(self):
        today = datetime.date.today()
        response = self.client.get(f"/{today.year}/{today.month}/{today.day}",follow=True)
        self.assertTemplateUsed(response, "home.html")