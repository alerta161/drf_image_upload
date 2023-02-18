from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class ImageUploadTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_image_upload_basic_tier(self):
        with open('/path/to/image.png', 'rb') as image:
            self.client.login(username='testuser', password='testpass')
            response = self.client.post('/api/images/', {'image': image, 'tier': 'basic'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['tier'], 'basic')