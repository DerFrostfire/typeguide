from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('typescript/modules/(?P<id>\d+)$', views.lesson, name='lesson'),
    path('', views.index, name=''),
]