# chatbot/urls.py
from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.chat_interface, name='chat_interface'),
    path('api/chat_message/', views.chat_api, name='chat_api'), # api
]