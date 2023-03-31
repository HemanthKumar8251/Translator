from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('T2T', views.T2T,name='T2T'),
    path('T2TR', views.T2TR,name='T2TR'),
    path('S2T', views.S2T,name='S2T')
]