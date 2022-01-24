from django.test import TestCase
from django.urls import resolve

from leaderboard.views import home_page
# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        home_view = resolve("/")
        self.assertEqual(home_view.func, home_page)
