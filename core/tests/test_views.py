#coding = utf-8
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_status_code(self):
        client = Client()
        response = client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        client = Client()
        response = client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')