from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('hell/', views.all_products, name='all_products'),
    path('product-detail/', views.product_detail, name='product_detail')
]