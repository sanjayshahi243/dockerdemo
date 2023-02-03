from django.db import models

# Create your models here.

class AppModel(models.Model):
    title = models.CharField(max_length=100, null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title
