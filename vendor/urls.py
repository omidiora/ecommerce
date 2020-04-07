from django.urls import path 
from vendor.views import ProductListView, ProductDetailView,ProductFeaturedListView,ProductFeaturedDetailView

urlpatterns = [

    path('',ProductListView.as_view()),
    path('product/<slug>', ProductDetailView.as_view() ),
    path('featured', ProductFeaturedListView.as_view()),
    path('featured/<slug>',ProductFeaturedDetailView.as_view()),
  

]