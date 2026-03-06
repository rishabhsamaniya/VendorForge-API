from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateDeleteView, CategoryListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('<int:pk>/', ProductUpdateDeleteView.as_view()),
    
]
