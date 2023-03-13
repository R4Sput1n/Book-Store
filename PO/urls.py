from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('account/', include('accounts.urls')),
    path('cart/', include('shopping_cart.urls')),
]
