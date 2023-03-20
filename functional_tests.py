from selenium import webdriver
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
        self.fail('Finish the test')

        # He is invited to enter a to-do item straight away

        # He types "Buy peacock feathers" into a text box

        # When he hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. He enters
        # "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on his list

        # Daniel wonders whether the site will remember his list. Then he sees
        # that the site has generated n unique URL for his -- there is some
        # explanatory text to that effect

        # He visits that URL - his to-do list is still there

        # Satisfied, he goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
