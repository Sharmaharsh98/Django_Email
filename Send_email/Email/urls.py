from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.Email_view, name = 'send')
]