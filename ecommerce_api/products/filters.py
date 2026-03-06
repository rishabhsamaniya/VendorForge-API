import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
     # Exact match (case insensitive)
     name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')

      # Contains match (like search but controlled)
     name_contains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

      # Price range
     min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
     max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')


     # Stock range
     min_stock = django_filters.NumberFilter(field_name='stock', lookup_expr='gte')
     max_stock = django_filters.NumberFilter(field_name='stock', lookup_expr='lte')

    #  Category
     category = django_filters.NumberFilter(field_name='category_id')


     class Meta:
          model = Product
          fields = []

     


    