from django.test import TestCase
from django.test.client import Client
import json

class TestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_api(self):
        string = {'string': 'hi, hi, hello'}
        string = json.dumps(string)
        response = self.c.post('/api/', content_type='application/json', data=string)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"hi":2, "hello":1})
