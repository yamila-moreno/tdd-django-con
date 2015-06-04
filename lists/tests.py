from django.http import HttpRequest
from django.test import TestCase

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn('<title>To-Do Lists</title>', response.content.decode())
        self.assertTrue(response.content.endswith(b'</html>'))
