from django.urls import path 
from vendor.views import ProductListView, ProductDetailView

urlpatterns = [

    path('',ProductListView.as_view()),
    path('product/<pk>',ProductDetailView.as_view()),
  

]