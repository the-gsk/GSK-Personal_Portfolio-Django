from django.urls import path
from . import views


app_name= 'portfolio'

urlpatterns = [
    path('', views.home, name='new_home'),
    path('old', views.old_home, name='home'),
    path('projects/',views.projects, name='projects_detail')

]