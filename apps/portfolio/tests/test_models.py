from django.test import TestCase
from apps.portfolio.models import Project

class ProjectModelTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            tech_stack="Django",
            is_published=True
        )

    def test_project_creation(self):
        self.assertEqual(self.project.title, "Test Project")
