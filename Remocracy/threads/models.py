from django.db import models

# Create your models here.
class Thread(models.Model):
	title = models.CharField(max_length=50)
	text = models.CharField(max_length=250)
	createDate = models.DateTimeField('date created')
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.title

class Comment(models.Model):
	text = models.CharField(max_length=250)
	createDate = models.DateTimeField('date created')
	votes = models.IntegerField(default=0)
	thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
	def __str__(self):
		return self.text[:25]
