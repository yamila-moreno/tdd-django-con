import unittest

from selenium import webdriver

class SimpleListTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()        

    def tearDown(self):
        self.browser.quit()
        
    def test_starting_a_todo_list(self):        
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        
if __name__ == '__main__':
    unittest.main()
