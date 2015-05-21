import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient

class DRFLabTest(TestCase):
    def test_invalid_fields_discarded(self):
        client = APIClient()
        url = reverse('customer')
        data = {
            'name': 'kamal',
            'extra': 'should be discarded',
        }
        response = client.post(url, data)
        response_json = json.loads(response.content)
        assert 'extra' not in response_json
