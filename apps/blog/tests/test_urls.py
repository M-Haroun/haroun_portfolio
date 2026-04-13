from django.test import TestCase
from django.urls import resolve,reverse
from apps.blog.views import (
    BlogListView, BlogDetailView,
    BlogCreateView,BlogUpdateView,
    BlogDeleteView,
)
from apps.blog.models import Post

# Create your tests here.

class TestUrls(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Project",
            content="Test Content",
        )
        
    # Test list url   
    def test_list_url_resolves(self):
       url = reverse('blog:list')  
       self.assertEqual(resolve(url).func.view_class,BlogListView)
    
    # Test detail url
    def test_detail_url_resolves(self):
       url = reverse('blog:detail',args=[self.post.slug])  
       self.assertEqual(resolve(url).func.view_class,BlogDetailView)
    
    # Test create url
    def test_create_url_resolves(self):
       url = reverse('blog:create')  
       self.assertEqual(resolve(url).func.view_class,BlogCreateView)
    
    # Test edit url
    def test_edit_url_resolves(self):
       url = reverse('blog:edit',args=[self.post.slug])  
       self.assertEqual(resolve(url).func.view_class,BlogUpdateView)
    
    # Test delete url
    def test_delete_url_resolves(self):
       url = reverse('blog:delete',args=[self.post.slug])  
       self.assertEqual(resolve(url).func.view_class,BlogDeleteView)
    