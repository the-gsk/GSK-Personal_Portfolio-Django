from distutils.command.upload import upload
from django.db import models


# Create your models here.

class Skill(models.Model):
    rank = models.IntegerField(unique=True)
    heading = models.BooleanField(default=True)
    skill_name = models.CharField(max_length=100)
    def __str__(self):
        return self.skill_name

class Project(models.Model):
    rank = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill,blank=True)
    description = models.TextField()
    heading = models.BooleanField(default=True)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    projects = models.ForeignKey(Project, related_name='images',on_delete=models.CASCADE)
    rank = models.IntegerField(unique=True)
    heading = models.BooleanField(default=True)
    image = models.ImageField(upload_to=f'project_images/', blank=True, null=True,default='project_images/default_project.jpg')
    def __str__(self):
        return self.projects.title
class ProjectResponsebility(models.Model):
    property = models.ForeignKey(Project, related_name='responsebility',on_delete=models.CASCADE)
    rank = models.IntegerField(unique=True)
    heading = models.BooleanField(default=True)
    response = models.TextField()