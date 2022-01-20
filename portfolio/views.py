from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render (request,'portfolio/home.html')


def projects(request):
    projects = Project.objects.all()
    return render (request,'portfolio/projects.html', {'projects':projects})
