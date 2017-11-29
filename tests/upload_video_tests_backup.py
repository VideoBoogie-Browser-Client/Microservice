# -*- coding: utf-8 -*-
"""Tests specific to the user actions of uploading video content in browser.

"""
from unittest import TestCase
from app.main import app


class UploadVideoTest(TestCase):
    """Represents all the test cases for the page where user uploads video.

    """
    def test_upload_url_responds_ok(self):
        """Test to verify that 'upload' page returns correct response.

        Based on the hard coded uri string, '/upload', the expected response
        status should be 200 (OK).
        """
        self.client = app.test_client()
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 200)

    def test_upload_video_contains_paragraph_with_instructions(self):
        """This test is verifying that the first paragraph exists.

        The content should contain the string 'submit your video' somewhere
        within the body of the page.

        .. note:: This is essentially testing for an existence of a constant.
        This kind of test is of a dubious value and should probably be deleted.
        """
        self.client = app.test_client()
        response = self.client.get('/upload')
        self.assertTrue('submit your video' in response.get_data(as_text=True))

    def test_next_sunday_date_should_be_sometime_in_the_future(self):
        """This should verify that the next sunday date is not in the past.

        Based on a given date, the test should confirm that the date to be
        displayed to the user is equal to some day in the future. The future
        time may also be the current day -- the current Sunday.
        """
        pass

    def test_based_on_current_date_should_find_next_sunday_date(self):
        """The test confirms that the next Sunday should fall on a correct
        calendar date."""
        pass
