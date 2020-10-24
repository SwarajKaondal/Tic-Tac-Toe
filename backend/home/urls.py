from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ajax/userInput/', views.userInput, name='userInput')
]
