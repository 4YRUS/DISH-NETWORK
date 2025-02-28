
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name = 'home'),
    path('mute/', views.mute, name = 'mute'),
    path('deaf/', views.deaf, name = 'deaf'),
]


