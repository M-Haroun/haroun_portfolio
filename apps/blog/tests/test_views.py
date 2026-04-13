from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.blog.models import Post, Comment
from apps.blog.forms import CommentForm

class PostListViewTest(TestCase):

    def setUp(self):
        self.published_post = Post.objects.create(
            title="Published Post",
            content="Content",
            published=True
        )
        self.unpublished_post = Post.objects.create(
            title="Draft Post",
            content="Content",
            published=False
        )

    def test_list_only_shows_published_posts(self):
        response = self.client.get(reverse('blog:list'))
        self.assertContains(response, "Published Post")
        self.assertNotContains(response, "Draft Post")
        self.assertEqual(response.status_code, 200)


class PostDetailViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="pass123"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="Content",
            published=True
        )
        # Comments
        self.comment_approved = Comment.objects.create(
            post=self.post, user=self.user, content="Approved", is_approved=True
        )
        self.comment_unapproved = Comment.objects.create(
            post=self.post, user=self.user, content="Unapproved", is_approved=False
        )

    def test_detail_view_contains_post_and_approved_comments(self):
        response = self.client.get(
            reverse('blog:detail', args=[self.post.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertContains(response, "Approved")
        self.assertNotContains(response, "Unapproved")
        self.assertIsInstance(response.context['form'], CommentForm)

    def test_detail_view_returns_404_for_invalid_slug(self):
        response = self.client.get(reverse('blog:detail', args=["non-existent-slug"]))
        self.assertEqual(response.status_code, 404)

    def test_post_comment_redirects_for_anonymous(self):
        response = self.client.post(
            reverse('blog:detail', args=[self.post.slug]),
            {"content": "New comment"}
        )
        self.assertEqual(response.status_code, 302)  # redirect to login