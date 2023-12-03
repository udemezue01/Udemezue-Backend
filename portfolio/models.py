from django.db import models

from django.conf import settings


class Portfolio(models.Model):

	user 			=  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
	title 			=  models.CharField(max_length = 3000)
	about 			=  models.CharField(max_length = 3000)
	image			=  models.ImageField(blank = True, null = True)

	def __str__(self):
		return self.title