from django.urls import path
from .views import fetch_shopify_orders

urlpatterns = [
    path("/orders", fetch_shopify_orders, name="fetch-shopify-orders"),
]
