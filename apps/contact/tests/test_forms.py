# apps/contact/tests/test_forms.py
from django.test import TestCase
from django.urls import reverse
from apps.contact.models import ContactMessage

class ContactFormTest(TestCase):
    """Tests for the contact form submission"""

    def test_contact_form_saves_message(self):
        """
        Submitting the contact form with valid data
        should create a ContactMessage and redirect.
        """
        data = {
            "name": "Haroun",
            "email": "test@test.com",
            "message": "Hello, this is a test message."
        }

        response = self.client.post(reverse("contact:contact"), data)

        # 1 Check that a new ContactMessage was created
        self.assertEqual(ContactMessage.objects.count(), 1)
        contact_message = ContactMessage.objects.first()
        self.assertEqual(contact_message.name, "Haroun")
        self.assertEqual(contact_message.email, "test@test.com")
        self.assertEqual(contact_message.message, "Hello, this is a test message.")

        # 2 Check that the view redirects (status code 302)
        self.assertEqual(response.status_code, 302)

    def test_contact_form_invalid_data(self):
        """
        Submitting the form with missing fields should not save a message.
        """
        data = {
            "name": "",  # missing name
            "email": "invalid_email",  # invalid email
            "message": ""
        }

        response = self.client.post(reverse("contact:contact"), data)

        # No messages should be created
        self.assertEqual(ContactMessage.objects.count(), 0)

        # The response should be 200 because form is usually re-rendered with errors
        self.assertEqual(response.status_code, 200)

        # Optionally, you can check that error messages appear in the context
        self.assertContains(response, "This field is required", status_code=200)