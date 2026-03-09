from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateDeleteView, CategoryListCreateView, UploadProductImageView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('<int:pk>/', ProductUpdateDeleteView.as_view()),
    path('upload-image/<int:product_id>/', UploadProductImageView.as_view()),
    
    
]
