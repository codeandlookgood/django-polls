from django.shortcuts import render

#From Tutorial01 : https://docs.djangoproject.com/en/2.1/intro/tutorial01/
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
