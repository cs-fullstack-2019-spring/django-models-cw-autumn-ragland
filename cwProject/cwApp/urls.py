from django.urls import path
from . import views
# default path
urlpatterns = [
    path('', views.index, name='index'),
]