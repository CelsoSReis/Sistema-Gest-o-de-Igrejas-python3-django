from django.urls import path
from autenticacao import views

urlpatterns = [ 
    path('', views.register, name='login'),
     
] 