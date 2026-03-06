from .views import RegisterView, VendorOnlyView
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('vendor-test/', VendorOnlyView.as_view(), name='vendor-test'),
]
