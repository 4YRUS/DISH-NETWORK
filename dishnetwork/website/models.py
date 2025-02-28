from django.db import models

class imagefield(models.Model):

	image = models.ImageField(upload_to="images/")

