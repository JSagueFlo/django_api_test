from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='raw_index'),
    path('test/', views.test_raw, name='raw_test'),
    path('test2/', views.test_raw_only_values, name='raw_test_only_values')
]
