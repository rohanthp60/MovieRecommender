from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rec', views.rec, name='rec'),
    path('spec', views.spec, name='spec')
]