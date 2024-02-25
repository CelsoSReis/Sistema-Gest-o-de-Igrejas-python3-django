from django.urls import path
# importa as views que foram criadas


# padrão django urls
urlpatterns = [
    path('endereco', MinhaView.as_view(), name='name-da-url'),
]