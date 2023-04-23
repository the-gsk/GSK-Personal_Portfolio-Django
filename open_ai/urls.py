from django.urls import path
from . import views


app_name= 'open_ai'

urlpatterns = [
    path('chat', views.chatresponse, name='ai-chat'),

]