from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 10

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
class NewVisitorTest(LiveServerTestCase):
    # Start browser
    def setUp(self):
        self.browser = webdriver.Firefox(options=options)

    # Stop browser
    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    # Test method
    def test_can_start_a_list_for_one_user(self):
        # Daniel has heard about a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get(self.live_server_url)

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
        # "1: Learn about how TDD works" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Learn about how TDD works')

        # There is still a text box inviting her to add another item. He enters
        # "Use TDD knowledge to write masters degree thesis"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use TDD knowledge to write masters degree thesis')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his list
        self.wait_for_row_in_list_table('1: Learn about how TDD works')
        self.wait_for_row_in_list_table('2: Use TDD knowledge to write masters degree thesis')

        # Daniel wonders whether the site will remember his list. Then he sees
        # that the site has generated n unique URL for his -- there is some
        # explanatory text to that effect

        # He visits that URL - his to-do list is still there

        # Satisfied, he goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Daniel starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Learn about how TDD works')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Learn about how TDD works')

        # She notices that her list has an unique URL
        daniel_list_url = self.browser.current_url
        self.assertRegex(daniel_list_url, '/lists/.+')

        # Now a new user, Andreea, comes along to the site

        ## Use a new broswer session to make sure no information
        ## of Daniel's coming from the cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox(options=options)

        # Andreea visits the home page. There is no sign of Daniel's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Learn about how TDD works', page_text)
        self.assertNotIn('Use TDD knowledge to write masters degree thesis', page_text)

        # Andreea starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Learn for microcontrollers exam')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Learn for microcontrollers exam')

        # Andreea gets his own unique URL too
        andreea_list_url = self.browser.current_url
        self.assertRegex(andreea_list_url, '/lists/.+')
        self.assertNotEqual(andreea_list_url, daniel_list_url)

        # Again, there isi no trace of Daniel's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Learn about how TDD works', page_text)
        self.assertIn('Learn for microcontrollers exam', page_text)

        # Satisfied, they both go back to sleep
