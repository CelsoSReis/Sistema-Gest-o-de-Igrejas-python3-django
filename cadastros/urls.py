from django.urls import path
# importa as views que foram criadas
from .views import PastorPresidenteCreate, SecretariosCreate

# padrão django urls
urlpatterns = [
    path('cadastrar/pastorpresidente', PastorPresidenteCreate.as_view(), name='cadastrar-pastor-presidente'),
    path('cadastrar/secretario', SecretariosCreate.as_view(), name='cadastrar-secretario'),
]