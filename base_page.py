import unittest
from selenium import webdriver

class Base_page(unittest.TestCase):
    chrome = webdriver.Chrome()

    def setUp(self):
        self.chrome.maximize_window()
        self.chrome.get('https://codepen.io/login')
        self.chrome.implicitly_wait(7)

    def tearDown(self):
        self.chrome.quit()


