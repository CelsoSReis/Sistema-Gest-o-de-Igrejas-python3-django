from django.urls import path
from . import views

urlpatterns = [
    path('dizimos/', views.dizimos, name='dizimos'),
    path('dizimos/editar/<int:dizimo_id>/', views.editar_dizimo, name='editar_dizimo'),
    path('dizimos/excluir/<int:dizimo_id>/', views.excluir_dizimo, name='excluir_dizimo'),

]