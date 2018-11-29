
from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.shoper_login, name='ShoperForm'),
    path('signup/', views.signup, name='signup'),
    path('signup1/', views.signup1, name='signup1'),
]
