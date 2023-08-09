from django.urls import path, include
from example.views import index

urlpatterns = [
    path('', index),
]