from django.urls import path
from mgr import customer

urlpatterns = [
    path('customer/', customer.dispatcher),
]

