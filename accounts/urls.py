from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views as account_views


urlpatterns = [
    path('', account_views.account, name='account'),
    path('register/', account_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/accounts/logout.html'), name='logout'),
    path('<profile>/', account_views.profile, name='profile')
]
