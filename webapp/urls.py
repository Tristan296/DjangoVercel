from django.urls import path, include
from webapp.views import index

urlpatterns = [
    path('', index),
]