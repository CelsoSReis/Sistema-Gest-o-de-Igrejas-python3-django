from django.urls import path
from . import views

urlpatterns = [
    path('dizimos/', views.dizimos, name='dizimos'),
]