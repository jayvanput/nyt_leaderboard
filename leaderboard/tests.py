from cmath import exp
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from leaderboard.views import home_page
# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        home_view = resolve("/")
        self.assertEqual(home_view.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string("home.html")
        self.assertEqual(response.content.decode(), expected_html)
