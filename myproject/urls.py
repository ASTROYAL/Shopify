from django.contrib import admin
from django.urls import path
from myapp.views import fetch_shopify_orders  # Adjust the import according to your app name

urlpatterns = [
    path('/admin/', admin.site.urls),
    path('/api/orders/', fetch_shopify_orders, name='fetch-shopify-orders'),  # Ensure this path is here
]
