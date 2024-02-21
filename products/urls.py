from django.urls import path
from products.views import (product_detail, product_list,
                            manufacturer_detail, manufacturer_list)

app_name = 'products'
urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name="product-detail"),
    path('manufacturers/', manufacturer_list, name="manufacturer-list"),
    path('manufacturers/<int:pk>', manufacturer_detail, name="manufacturer-detail"),
    ]
    
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)