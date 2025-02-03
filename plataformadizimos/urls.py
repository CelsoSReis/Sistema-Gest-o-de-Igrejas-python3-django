from django.urls import path
from . import views
from .views import dizimos, editar_dizimo

urlpatterns = [
    path('dizimos/', views.dizimos, name='dizimos'),
    path('dizimos/editar/<int:dizimo_id>/', editar_dizimo, name='editar_dizimo'),
]