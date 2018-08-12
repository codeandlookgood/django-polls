from django.db import models

import datetime #From Tutorial02: https://docs.djangoproject.com/en/2.1/intro/tutorial02/
from django.utils import timezone #From Tutorial02: https://docs.djangoproject.com/en/2.1/intro/tutorial02/


#From Tutorial02: https://docs.djangoproject.com/en/2.1/intro/tutorial02/
class Question(models.Model): #ERROR Made: Double Point after class brackets!!
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
		
	def was_published_recently(self): #From Tutorial02: https://docs.djangoproject.com/en/2.1/intro/tutorial02/
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

		