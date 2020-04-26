from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUser(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return str(self.user)

class Thread(models.Model):
	title = models.CharField(max_length=50)
	text = models.CharField(max_length=250)
	createDate = models.DateTimeField('date created')
	votes = models.IntegerField(default=0)
	siteUser = models.ForeignKey(SiteUser,on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class Comment(models.Model):
	text = models.CharField(max_length=250)
	createDate = models.DateTimeField('date created')
	votes = models.IntegerField(default=0)
	thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
	siteUser = models.ForeignKey(SiteUser,on_delete=models.CASCADE)
	def __str__(self):
		return self.text[:25]
