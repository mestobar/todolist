from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, blank =False, null=False)
    completed= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}" 
