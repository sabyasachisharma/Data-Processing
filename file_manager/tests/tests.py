from django.test import TestCase
from django.urls import reverse

class FileManagerTests(TestCase):
    def test_upload_page(self):
        response = self.client.get(reverse('file_upload'))
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_page(self):
        response = self.client.get(reverse('file_dashboard'))
        self.assertEqual(response.status_code, 200)
