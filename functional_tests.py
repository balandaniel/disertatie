from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# browser = webdriver.Firefox(options=options)
#
# # Daniel has heard about a cool new online to-do app
# # Daniel wants to check the homepage
# browser.get('http://localhost:8000')
#
# # He notices the page title and header mention to-do list
# assert 'To-Do' in browser.title, "Browser tittle was " + browser.title
#
# # He is invited to enter a to-do item straight away
#
# # He types "Buy peacock feathers" into a text box
#
# # When he hits enter, the page updates, and now the page lists
# # "1. Buy peacock feathers" as an item in a to-do list
#
# # There is still a text box inviting her to add another item. He enters
# # "Use peacock feathers to make a fly"
#
# # The page updates again, and now shows both items on his list
#
# # Daniel wonders whether the site will remember his list. Then he sees
# # that the site has generated n unique URL for his -- there is some
# # explanatory text to that effect
#
# # He visits that URL - his to-do list is still there
#
# # Satisfied, he goes back to sleep
#
# browser.quit()


# Tests are organized into classes, as the example below
class NewVisitorTest(unittest.TestCase):
    # Start browser
    def setUp(self):
        self.browser = webdriver.Firefox(options=options)

    # Stop browser
    def tearDown(self):
        self.browser.quit()

    # Test method
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Daniel has heard about a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page tittle and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Learn about how TDD works" into a text box
        inputbox.send_keys('Learn about how TDD works')

        # When he hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        #self.assertTrue(
            #any(row.text == '1: Learn about how TDD works' for row in rows),
            #f"New to-do item did not appear in table. Contents were:\n{table.text}"
        #)

        self.assertIn('1: Learn about how TDD works', [row.text for row in rows])

        # There is still a text box inviting her to add another item. He enters
        # "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use TDD knowledge to write masters degree thesis')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        # The page updates again, and now shows both items on his list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Learn about how TDD works', [row.text for row in rows])
        self.assertIn(
            '2: Use TDD knowledge to write masters degree thesis',
            [row.text for row in rows]
        )

        # Daniel wonders whether the site will remember his list. Then he sees
        # that the site has generated n unique URL for his -- there is some
        # explanatory text to that effect
        self.fail('Finish the test!')

        # He visits that URL - his to-do list is still there

        # Satisfied, he goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
