from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shopping_cart import views as cart_views

urlpatterns = [
    path('', cart_views.cart, name='cart'),
    # path('<customer_id>/', cart_views.cart_with_id, name='cart_with_id'),
    path('del/product_<product_id>/', cart_views.delete_from_cart, name='delete_from_cart'),
    path('clear/', cart_views.clear_cart, name='clear_cart'),
    path('buy/', cart_views.buy_products, name='buy'),
    path('add/product_<product_id>/', cart_views.add_to_cart, name='add_order'),
    path('add/product_<product_id>/redir', cart_views.add_and_redirect_to_cart, name='add_and_redirect')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
