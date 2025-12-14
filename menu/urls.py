from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('add/', views.menu_add, name='menu_add'),
    path('delete/<int:item_id>/', views.menu_delete, name='menu_delete'),
    path('<int:item_id>/', views.menu_detail, name='menu_detail'),
]