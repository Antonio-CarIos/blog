from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('detalhes/<int:pk>', views.detalhes,name='detalhes'),
   
]



