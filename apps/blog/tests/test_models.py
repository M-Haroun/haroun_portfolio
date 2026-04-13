from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.blog.models import Post, Comment

class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="My First Post",
            content="Test content"
        )

    def test_slug_is_generated(self):
        self.assertEqual(self.post.slug, "my-first-post")

    def test_post_str(self):
        self.assertEqual(str(self.post), "My First Post")

    def test_default_published_is_true(self):
        self.assertTrue(self.post.published)

    def test_slug_not_overwritten_if_exists(self):
        post = Post.objects.create(
            title="Another Post",
            slug="custom-slug",
            content="Content"
        )
        self.assertEqual(post.slug, "custom-slug")




class CommentModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="pass123"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="Content"
        )

    def test_comment_creation(self):
        comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            content="Nice post!"
        )
        self.assertFalse(comment.is_approved)
        self.assertEqual(str(comment), "testuser - Test Post")