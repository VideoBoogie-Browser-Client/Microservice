import time
from selenium import webdriver
from unittest import TestCase


# TODO: Delete the redundant 'virtualenv' directory which is no longer needed.
class UploadVideoTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_video_upload_page_has_intro_paragraph_with_correct_content(self):
        # A user arrives at the page where he can upload video.
        self.browser.get('http:127.0.0.1:5000/upload')

        # The user notices some instruction on submitting video to contest.
        intro = self.browser.find_element_by_id("top-intro")
        self.assertIn('submit your video', intro.text)

        # The user also notices a link to help pages.

        # When he clicks on the link he is redirected to the help pages.

        # Next, the user notices there is an input box on the page where he can
        # type in the caption for his video.
