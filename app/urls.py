from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasbih, name='tasbih'),
    path('main/', views.index, name='home'),
]