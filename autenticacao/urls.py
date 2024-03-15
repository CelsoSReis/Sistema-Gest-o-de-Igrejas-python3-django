from django.urls import path
from django.contrib.auth import views as auth_views



# padrão django urls
urlpatterns = [
 path('login/', auth_views.LoginView.as_view(
     template_name='autenticacao/form.html'
 ), name="login"),
]