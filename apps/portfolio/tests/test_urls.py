from django.test import TestCase
from django.urls import resolve,reverse
from apps.portfolio.views import (
    ProjectListView,ProjectDetailView,
    ProjectCreateView, ProjectUpdateView,
    ProjectDeleteView
)
from apps.portfolio.models import Project

# Create your tests here.

class TestUrls(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            tech_stack="Django",
            is_published=True
        )
        
    # Test list url   
    def test_list_url_resolves(self):
       url = reverse('portfolio:list')  
       self.assertEqual(resolve(url).func.view_class,ProjectListView)
    
    # Test detail url
    def test_detail_url_resolves(self):
       url = reverse('portfolio:detail',args=[self.project.pk])  
       self.assertEqual(resolve(url).func.view_class,ProjectDetailView)
    
    # Test create url
    def test_create_url_resolves(self):
       url = reverse('portfolio:create')  
       self.assertEqual(resolve(url).func.view_class,ProjectCreateView)
    
    # Test update url
    def test_update_url_resolves(self):
       url = reverse('portfolio:update',args=[self.project.pk])  
       self.assertEqual(resolve(url).func.view_class,ProjectUpdateView)
    
    # Test delete url
    def test_delete_url_resolves(self):
       url = reverse('portfolio:delete',args=[self.project.pk])  
       self.assertEqual(resolve(url).func.view_class,ProjectDeleteView)
    