from rest_framework.response import Response
from rest_framework.decorators import api_view
import shopify

@api_view(['GET'])
def get_orders(request):
    
    shop_url = "your-shop-name.myshopify.com"
    access_token = "your-shopify-access-token"
    api_key = '0cfd2f318e1a90a633dfabf5b2222c9d'
    secret = '8a9133c5d309bb7c0e5e28fe6023f81f'

    # Set up Shopify session
    shopify.Session.setup(api_key, secret)
    session = shopify.Session(shop_url, "2023-10", access_token)
    shopify.ShopifyResource.activate_session(session)

    # Fetch orders
    orders = shopify.Order.find()
    
    # Convert orders to a list of dictionaries
    order_data = []
    for order in orders:
        order_data.append({
            "id": order.id,
            "email": order.email,
            "total_price": order.total_price,
            "created_at": order.created_at
        })

    return Response(order_data)
