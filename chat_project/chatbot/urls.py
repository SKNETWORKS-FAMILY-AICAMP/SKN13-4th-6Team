from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_interface, name='chat_interface'),
    path('api/chat_message/<str:message>', views.chat_api, name='chat_api'),
]