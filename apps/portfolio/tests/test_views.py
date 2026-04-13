from django.test import TestCase
from django.urls import reverse
from apps.portfolio.models import Project


class ProjectListViewTest(TestCase):

    def test_project_list_view(self):
        response = self.client.get(reverse('portfolio:list'))
        self.assertEqual(response.status_code, 200)

class ProjectDetailViewTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            tech_stack="Django",
            is_published=True
        )
    
    def test_project_detail_view(self):
        response = self.client.get(
            reverse('portfolio:detail', args=[self.project.pk])
        )
        self.assertEqual(response.status_code, 200)
    
    def test_project_detail_view_404(self):
        response = self.client.get(
            reverse('portfolio:detail', args=[999])
        )
        self.assertEqual(response.status_code, 404)