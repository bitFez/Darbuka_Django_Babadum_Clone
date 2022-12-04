from django.db import models

# Create your models here.
class Language(models.Model):
    lan_name = models.CharField(max_length=100)