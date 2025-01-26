
from django.test import TestCase
from django.urls import reverse

class FileUploadViewTests(TestCase):
    def test_upload_view_status_code(self):
        response = self.client.get(reverse('file_upload'))
        self.assertEqual(response.status_code, 200)
