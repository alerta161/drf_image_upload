from django.urls import path, include
from . import views

urlpatterns = [
    path('images/', views.ImageViewSet.as_view({'get': 'list'}), name='images'),
]
