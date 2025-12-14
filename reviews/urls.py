from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_list, name='reviews'),
    path('add/', views.review_add, name='review_add'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
]