from django.urls import path
from django.contrib.auth import views as auth_views, logout

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='autenticacao/form.html'
    ), name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout'),
]
