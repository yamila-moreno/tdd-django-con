from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page_view_uses_home_template(self):
        request = HttpRequest()
        response = home_page(request)
        template = render_to_string('home.html')
        self.assertEqual(response.content.decode('utf8'), template)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn('<title>To-Do Lists</title>', response.content.decode())
        self.assertTrue(response.content.strip().endswith(b'</html>'))
