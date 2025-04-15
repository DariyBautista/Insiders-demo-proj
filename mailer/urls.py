from django.urls import path
from . import views

app_name = 'mailer'

urlpatterns = [
    path('', views.subscribe_view, name='mailer'),
    path('subscribe-success/', views.subscribe_success_view, name='subscribe-success'),
]
