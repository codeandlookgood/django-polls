#From Tutorial01 : c
from . import views
from django.urls import path
urlpatterns = [
	path('', views.index, name='index'),
]