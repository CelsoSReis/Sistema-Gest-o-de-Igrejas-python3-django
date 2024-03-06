from django.urls import path

urlpatterns = [
     path('endereco', MinhaView.as_view(), name='name-da-url'),
]