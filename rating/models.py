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
	# TODO: rename to attendance!
	poseshenie = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)]) 
	last_month_position = models.IntegerField()
	position_current = models.IntegerField()
	rating_upfoundation = models.IntegerField()
	txt_for_page = models.TextField(max_length=2500)
	# party

	def __str__(self):
		return self.name
	
	def position_change(self):
		return self.last_month_position - self.position_current

	def position_change_snippet(self):
		difference =  self.last_month_position - self.position_current
		if difference > 0:
			return f'<span class="difference positive">+{difference}</span>'
		elif difference < 0:
			return f'<span class="difference negative">{difference}</span>'
		else:
			return ''
	

	
