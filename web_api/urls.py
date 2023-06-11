from django.urls import path
from . import views



app_name= 'open_ai'

urlpatterns = [
    path('chat/', views.chatresponse, name='ai-chat'),
    path('universal_response/', views.universal_response, name='universal_response'),
    path('send-email/', views.send_email, name='send_email')

]