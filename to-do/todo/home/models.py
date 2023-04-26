from django.db import models

# Create your models here.
class tasks(models.Model):
    name = models.TextField(null=False)
    time = models.DateTimeField(auto_now_add=True)
    