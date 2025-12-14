from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Simple password reset (djongo-safe)
    path('password-reset/', views.password_reset_simple, name='password_reset'),
]