from django.test import SimpleTestCase
from django.urls import resolve,reverse
from apps.contact.views import ContactCreateView, ContactSuccessView

class TestUrls(SimpleTestCase):
    
    def test_contact_url_resolves(self):
        url = reverse('contact:contact')
        self.assertEquals(resolve(url).func.view_class,ContactCreateView)
    
    def test_success_url_resolves(self):
        url = reverse('contact:success')
        self.assertEquals(resolve(url).func.view_class,ContactSuccessView)