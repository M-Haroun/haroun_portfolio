from django.test import SimpleTestCase
from django.urls import resolve,reverse
from apps.core.views import index

class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url=reverse('index')
        self.assertEqual(resolve(url).func,index)