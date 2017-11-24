from unittest import TestCase
from bc.bc import app


# TODO Reorganize application project directory structure
class UploadVideoTest(TestCase):
    def test_upload_url_responds_ok(self):
        self.client = app.test_client()
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 200)

    def test_upload_video_contains_paragraph_with_instructions(self):
        self.client = app.test_client()
        response = self.client.get('/upload')
        self.assertTrue('submit your video' in response.get_data(as_text=True))
