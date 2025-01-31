# myproject/urls.py
from django.contrib import admin
from django.urls import include, path
from myapp import views  
from myapp.views import (
    fetch_shopify_orders,  
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  
    path('', views.home),  
    
    path('api/orders/', fetch_shopify_orders, name='fetch-shopify-orders'), 

]
