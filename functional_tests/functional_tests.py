import time
from selenium import webdriver
from unittest import TestCase


class UploadVideoTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

