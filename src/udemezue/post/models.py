from django.db import models
from django.conf import settings
# Create your models here.




class Post(models.Model):

	user 			=  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	title 			=  models.CharField(max_length = 3000)
	slug 			=  models.SlugField(max_length = 3000, blank = True, null = True)
	content			=  models.CharField(max_length = 30000)
	image 			=  models.ImageField(upload_to='images/', blank = True)

	def __str__(self):

		return self.title