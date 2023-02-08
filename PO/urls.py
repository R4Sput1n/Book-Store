from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from accounts import views as account_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('register/', account_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('account/', account_views.account, name='account'),
    path('cart/', include('shopping_cart.urls')),
]
