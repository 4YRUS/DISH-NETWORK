from django.db import models

class imagefield(models.Model):

	image = models.ImageField(upload_to="images/")

class audiofield(models.Model):

	audio = models.FileField(upload_to='audio/')