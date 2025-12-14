from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('item/<int:item_id>/update/', views.update_item, name='update_item'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('place/', views.place_order, name='place_order'),
    path('history/', views.orders_history, name='orders_history'),
    path('cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
]