from django.urls import path
# importa as views que foram criadas
from .views import PastorPresidenteCreate, SecretariosCreate, TesoureiroCreate, PastoresCreate, IgrejasCreate, CargoCreate, MembrosCreate
from .views import PastorPresidenteUpdate, SecretariosUpdate, TesoureiroUpdate, PastoresUpdate,IgrejasUpdate, CargoUpdate, MembrosUpdate

# padrão django urls
urlpatterns = [
    path('cadastrar/pastorpresidente', PastorPresidenteCreate.as_view(), name='cadastrar-pastor-presidente'),
    path('cadastrar/secretario', SecretariosCreate.as_view(), name='cadastrar-secretario'),
    path('cadastrar/tesoureiro', TesoureiroCreate.as_view(), name='cadastrar-tesoureiro'),
    path('cadastrar/pastores', PastoresCreate.as_view(), name='cadastrar-pastores'),
    path('cadastrar/igrejas', IgrejasCreate.as_view(), name='cadastrar-igrejas'),
    path('cadastrar/cargos', CargoCreate.as_view(), name='cadastrar-cargos'),
    path('cadastrar/membros', MembrosCreate.as_view(), name='cadastrar-membros'),

## Editar registos
    path('editar/pastorpresidente/<int:pk>/', PastorPresidenteUpdate.as_view(), name='editar-pastor-presidente'),
    path('editar/secretario/<int:pk>/', SecretariosUpdate.as_view(), name='editar-secretario'),

]