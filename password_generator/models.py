from django.db import models

# Create your models here.

class Guide(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    assurance = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return  self.title