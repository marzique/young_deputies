from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import os


# Create your models here.

class Deputy(models.Model):
	rada_id = models.IntegerField()
	name = models.CharField(max_length=200) # "Порошенко Петро "
	laws = models.IntegerField()
	photo = models.CharField(max_length=200)
	monitoring = models.IntegerField()
	poseshenie = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	last_month_position = models.IntegerField()
	position_current = models.IntegerField()
	rating_upfoundation = models.IntegerField()
	txt_for_page = models.TextField(max_length=2500)

	def __str__(self):
		return self.name


