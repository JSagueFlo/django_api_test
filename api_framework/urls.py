from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='framework_index'),
    path('test/', views.Test.as_view(), name='framework_test'),
]
