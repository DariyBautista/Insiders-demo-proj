from django.urls import path, include
from .views import dashboard_view

urlpatterns = [
    path('', include('allauth.urls')),
    path('dashboard/', dashboard_view, name='dashboard'),
]
