from django.test import TestCase
from django.urls import resolve

from authentication import views
import re
# Create your tests here.

class AuthenticationTest(TestCase):
    
    @staticmethod
    def remove_csrf(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_code)

    def assertEqualExceptCSRF(self, html_code1, html_code2):
        return self.assertEqual(
            self.remove_csrf(html_code1),
            self.remove_csrf(html_code2)
        )

    def test_auth_resolves_to_login_page(self):
        auth_view = resolve("/auth/")
        self.assertEqual(auth_view.func.view_class, views.Auth)