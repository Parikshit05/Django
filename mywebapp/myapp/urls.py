from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('show/', views.show, name='show'),
    path('dikhrhahai/', views.dikhrhahai, name='dikhrhahai'),
]