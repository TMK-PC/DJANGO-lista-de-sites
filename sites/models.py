from django.db import models

# Create your models here.

class Sites(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    url = models.TextField()
