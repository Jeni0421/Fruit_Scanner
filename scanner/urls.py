# scanner/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This links to the index view
    path('scan/', views.camera_scan, name='camera_scan'),
    # Add other URL patterns if needed
]

