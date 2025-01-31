import shopify


# myapp/views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

#from .shopify_config import API_KEY, PASSWORD, SHOP_URL


def get_orders(request):
    
    dummy_orders = [
        {
            "order_id": 123,
            "customer": "John Doe",
            "total": 59.99
        },
        {
            "order_id": 124,
            "customer": "Jane Doe",
            "total": 99.99
        }
    ]
    return JsonResponse(dummy_orders, safe=False)
# myapp/views.py


def home(request):
    
    return HttpResponse("Welcome to the API Home Page!This is shopify API")




# Shopify API connection setup
def connect_shopify():
    # shopify_config.py

    SHOP_URL = 'https://admin.shopify.com/store/kqbhdz-qq'  
    API_KEY = '0cfd2f318e1a90a633dfabf5b2222c9d'
    PASSWORD = '8a9133c5d309bb7c0e5e28fe6023f81f'

    shop_url = f"https://{API_KEY}:{PASSWORD}@{SHOP_URL}/admin/api/2021-01"
    shopify.ShopifyResource.set_site(shop_url)

# Fetch orders from Shopify
def fetch_shopify_orders(request):
    print("in shopify order func")
    
    #shop_url = 'https://admin.shopify.com/store/kqbhdz-qq'
    api_key = '0cfd2f318e1a90a633dfabf5b2222c9d'
    password = '8a9133c5d309bb7c0e5e28fe6023f81f'

    # Set up the Shopify API connection
    shop_url = "https://%s:%s@Abhishek.myshopify.com/admin" % (api_key, password)
    shopify.ShopifyResource.set_site(shop_url)
    print("he2y")

    # Fetch the orders
    orders = shopify.Order.find()
    #print("orders",orders)

    
    order_data = [{'id': order.id, 'name': order.name} for order in orders]
    print("hey1")
    return HttpResponse("Welcome to the API Page!")
    return JsonResponse(order_data, safe=False)



