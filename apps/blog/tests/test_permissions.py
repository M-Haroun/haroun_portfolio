from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from apps.blog.models import Post


class BlogPermissionTest(TestCase):

    def setUp(self):
        User = get_user_model()

        # Normal user (no permissions)
        self.normal_user = User.objects.create_user(
            username="user",
            password="1234"
        )

        # Superuser (has all permissions automatically)
        self.super_user = User.objects.create_superuser(
            username="admin",
            password="1234"
        )

        # Staff user (needs manual permission assignment)
        self.staff_user = User.objects.create_user(
            username="staff",
            password="1234",
            is_staff=True
        )

        # Assign permissions to staff user
        content_type = ContentType.objects.get_for_model(Post)

        add_permission = Permission.objects.get(
            codename="add_post",
            content_type=content_type
        )

        change_permission = Permission.objects.get(
            codename="change_post",
            content_type=content_type
        )

        delete_permission = Permission.objects.get(
            codename="delete_post",
            content_type=content_type
        )

        self.staff_user.user_permissions.add(
            add_permission,
            change_permission,
            delete_permission
        )

        # Create a post for update/delete tests
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content"
        )

    # -----------------------
    # NORMAL USER TESTS
    # -----------------------

    def test_normal_user_cannot_create_post(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(reverse("blog:create"))
        self.assertEqual(response.status_code, 403)

    def test_normal_user_cannot_edit_post(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(
            reverse("blog:edit", args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 403)

    def test_normal_user_cannot_delete_post(self):
        self.client.login(username="user", password="1234")
        response = self.client.post(
            reverse("blog:delete", args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 403)

    # -----------------------
    # STAFF USER TESTS
    # -----------------------

    def test_staff_user_can_create_post(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get(reverse("blog:create"))
        self.assertEqual(response.status_code, 200)

    def test_staff_user_can_edit_post(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get(
            reverse("blog:edit", args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_staff_user_can_delete_post(self):
        self.client.login(username="staff", password="1234")
        response = self.client.post(
            reverse("blog:delete", args=[self.post.slug])
        )
        self.assertIn(response.status_code, [200, 302])

    # -----------------------
    # SUPERUSER TESTS
    # -----------------------

    def test_superuser_can_create_post(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get(reverse("blog:create"))
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_edit_post(self):
        self.client.login(username="admin", password="1234")
        response = self.client.get(
            reverse("blog:edit", args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_delete_post(self):
        self.client.login(username="admin", password="1234")
        response = self.client.post(
            reverse("blog:delete", args=[self.post.slug])
        )
        self.assertIn(response.status_code, [200, 302])
