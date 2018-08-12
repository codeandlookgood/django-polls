from django.contrib import admin

#From Tutorial02: https://docs.djangoproject.com/en/2.1/intro/tutorial02/
from .models import Question 
admin.site.register(Question)
