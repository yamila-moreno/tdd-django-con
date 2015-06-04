import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SimpleListTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_todo_list(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        inputbox = self.browser.find_element_by_id('id_item_input')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Buy peackock feathers')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

if __name__ == '__main__':
    unittest.main(warnings='ignore')
