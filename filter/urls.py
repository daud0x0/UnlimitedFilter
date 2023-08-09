from django.urls import path
from . import views

app_name = "filter"

urlpatterns = [
        path('', views.home, name='home')
        ]
