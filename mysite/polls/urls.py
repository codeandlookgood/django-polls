#From Tutorial01 : https://docs.djangoproject.com/en/2.1/intro/tutorial01/
from . import views
from django.urls import path
urlpatterns = [
	path('', views.index, name='index'),
]