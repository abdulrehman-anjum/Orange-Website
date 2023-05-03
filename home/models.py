from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255, unique=True)
	phone_number = models.CharField(max_length=13)
	department = models.CharField(max_length=255)

	def __str__(self):
		return self.name