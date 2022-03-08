from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from leaderboard.views import home_page

import re
# Create your tests here.


class HomePageTest(TestCase):

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
        response = home_page(request)
        expected_html = render_to_string("home.html", request=request)
        self.assertEqualExceptCSRF(response.content.decode(), expected_html)

    def test_POST_redirects_to_current_page(self):
        response = self.client.post(
            "/post_time/", data={"username": "alice", "hours": "0", "minutes": "10", "seconds": "5"})
        print(response)
        self.assertRedirects(response, "/")
