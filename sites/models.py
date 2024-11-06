from django.db import models

# Create your models here.

class Sites(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    url = models.TextField()
    icon = models.ImageField(upload_to='media/', blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.icon.delete(save=False)
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.name
