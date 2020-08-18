from django.conf import settings
from django.db import models

# Create your models here.

class Car(models.Model):
	name_auto = models.CharField(max_length=50)
	model_auto = models.CharField(max_length=100)
	year = models.IntegerField()
	color = models.CharField(max_length=50)
	engine_capacity = models.FloatField()
	transmission = models.CharField(max_length=50)
	length = models.CharField(max_length=15)
	width = models.CharField(max_length=15)
	height = models.CharField(max_length=15)
	clearance = models.CharField(max_length=15)

	class Meta():
		verbose_name = 'Машина'
		verbose_name_plural = 'Машины'

	def __str__(self):
		return (str(self.model_auto) + ' ' + str(self.year))