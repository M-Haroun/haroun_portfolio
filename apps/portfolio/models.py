from django.db import models

# Create your models here.

class Project(models.Model):
    project_status = [
        ('Published','Published'),
        ('Completed','Completed'),
        ('Work on','Work on'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=700)
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(null=True,  blank=True,)
    live_demo = models.URLField(null=True,  blank=True,)
    image = models.ImageField(upload_to='photos/main_project_photos')
    status = models.CharField(max_length=50, null=True,  blank=True, choices= project_status)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # creation timestamp
    last_updated = models.DateTimeField(auto_now=True)    # update timestamp
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created_at"]  # last first
        
#To add more image for one project
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='photos/project_photos', null=True,  blank=True)