from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('rpa/', views.iniciar_rpa, name='iniciar_rpa'),
]