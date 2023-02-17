from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.getAllCategory),
    path('categories/<int:id>/', views.getCategory),
    path('products/', views.getAllProduct),
    path('products/<int:id>/', views.getProduct),
    path('categories/<int:id>/products', views.getProductsByCategory)
]