from django.urls import path, include
from .views import *


urlpatterns = [
    path('about/', about),
    path('index/', index),
    path('all_the_time/<str:name>', all_the_time),
    path('upload/', upload_image, name='upload_image'),
    path('list_of_products', ListOfProducts.as_view()),
    path('list_of_orders', ListOfOrders.as_view()),
    path('list_of_clients', ListOfClients.as_view()),
    path('product/<int:pk>', DetailProduct.as_view()),
    path('order/<int:pk>', DetailOrder.as_view()),
    path('client/<int:pk>', DetailClient.as_view()),
    #path('__debug__/', include("debug_toolbar.urls")),
]

