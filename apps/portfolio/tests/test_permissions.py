from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.portfolio.models import Project


class ProjectPermissionTest(TestCase):

    def setUp(self):
        User = get_user_model()

        self.normal_user = User.objects.create_user(
            username="user",
            password="1234"
        )

        self.super_user = User.objects.create_superuser(
            username="admin",
            password="1234"
        )

        # Staff user (NO project permissions assigned)
        self.staff_user = User.objects.create_user(
            username="staff",
            password="1234",
            is_staff=True
        )

        # Create project instance for update/delete tests
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description"
        )

    # -----------------------
    # NORMAL USER
    # -----------------------

    def test_normal_user_cannot_access_create(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(reverse('portfolio:create'))
        self.assertEqual(response.status_code, 403)

    def test_normal_user_cannot_update_project(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(
            reverse('portfolio:update', args=[self.project.id])
        )
        self.assertEqual(response.status_code, 403)

    def test_normal_user_cannot_delete_project(self):
        self.client.login(username="user", password="1234")
        response = self.client.post(
            reverse('portfolio:delete', args=[self.project.id])
        )
        self.assertEqual(response.status_code, 403)

    # -----------------------
    # STAFF USER (NO PERMISSIONS)
    # -----------------------

    def test_staff_user_cannot_access_create(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get(reverse('portfolio:create'))
        self.assertEqual(response.status_code, 403)

    def test_staff_user_cannot_update_project(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get(
            reverse('portfolio:update', args=[self.project.id])
        )
        self.assertEqual(response.status_code, 403)

    def test_staff_user_cannot_delete_project(self):
        self.client.login(username="staff", password="1234")
        response = self.client.post(
            reverse('portfolio:delete', args=[self.project.id])
        )
        self.assertEqual(response.status_code, 403)

    # -----------------------
    # SUPERUSER
    # -----------------------

    def test_superuser_can_access_create(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get(reverse('portfolio:create'))
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_update_project(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get(
            reverse('portfolio:update', args=[self.project.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_delete_project(self):
        self.client.login(username="admin", password="1234")
        response = self.client.post(
            reverse('portfolio:delete', args=[self.project.id])
        )
        self.assertIn(response.status_code, [200, 302])
