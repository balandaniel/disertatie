from selenium import webdriver

browser = webdriver.Firefox()  # start selenium webdriver to popup a real Firefox browser window
browser.get('http://localhost:8000') #

assert 'Django' in browser.title # check that the page has word "Django" in its title