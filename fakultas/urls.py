from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fkip/', views.fkip, name='fkip'),
    path('fh/', views.fh, name='fh'),
    path('ft/', views.ft, name='ft'),
]