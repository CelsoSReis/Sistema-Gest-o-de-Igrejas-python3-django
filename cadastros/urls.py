from django.urls import path
# importa as views que foram criadas
from .views import PastorPresidenteCreate, SecretariosCreate, TesoureiroCreate, PastoresCreate, IgrejasCreate, CargoCreate, MembrosCreate
from .views import PastorPresidenteUpdate, SecretariosUpdate, TesoureiroUpdate, PastoresUpdate,IgrejasUpdate, CargoUpdate, MembrosUpdate
from .views import PastorPresidenteDelete, SecretariosDelete, TesoureiroDelete, PastoresDelete, IgrejasDelete, CargoDelete, MembrosDelete
from .views import PastoresList, SecretariosList, TesoureiroList, PastorPresidenteList, IgrejasList, CargoList, MembrosList

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
    path('editar/tesoureiro/<int:pk>/', TesoureiroUpdate.as_view(), name='editar-tesoureiro'),
    path('editar/pastores/<int:pk>/', PastoresUpdate.as_view(), name='editar-pastores'),
    path('editar/igrejas/<int:pk>/', IgrejasUpdate.as_view(), name='editar-igrejas'),
    path('editar/cargos/<int:pk>/', CargoUpdate.as_view(), name='editar-cargos'),
    path('editar/membros/<int:pk>/', MembrosUpdate.as_view(), name='editar-membros'),

## Deletar registos
    path('excluir/pastorpresidente/<int:pk>/', PastorPresidenteDelete.as_view(), name='excluir-pastor-presidente'),
    path('excluir/secretario/<int:pk>/', SecretariosDelete.as_view(), name='excluir-secretario'),
    path('excluir/tesoureiro/<int:pk>/', TesoureiroDelete.as_view(), name='excluir-tesoureiro'),
    path('excluir/pastores/<int:pk>/', PastoresDelete.as_view(), name='excluir-pastores'),
    path('excluir/igrejas/<int:pk>/', IgrejasDelete.as_view(), name='excluir-igrejas'),
    path('excluir/cargos/<int:pk>/', CargoDelete.as_view(), name='excluir-cargos'),
    path('excluir/membros/<int:pk>/', MembrosDelete.as_view(), name='excluir-membros'),

## Listar Registros do banco de dados
    path('listar/pastorpresidente/<int:pk>/', PastorPresidenteList.as_view(), name='listar-pastor-presidente'),
    path('listar/secretario/', SecretariosList, name='listar-secretario'),
    path('listar/tesoureiro/', TesoureiroList, name='listar-tesoureiro'),
    path('listar/pastores/', PastoresList, name='listar-pastores'),
    path('listar/igrejas/', IgrejasList, name='listar-igrejas'),
    path('listar/cargos/', CargoList, name='listar-cargos'),
#    path('listar/cargos/<int:pk>/', CargoList, name='listar-cargos'),
    path('listar/membros/<int:pk>/', MembrosList.as_view(), name='listar-membros'),
]