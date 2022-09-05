from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_lisy_by_category'),
    path('product/<slug>/', views.product_detail, name='product_detail'),
]