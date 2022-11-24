from datetime import date
from pyexpat import model
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    title = models.IntegerField(max_length=0, null=True)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3)
    founded_at = models.DateField(null = True)

    def __repr__(self):
        return f'<{self.id} {self.name} - {self.fifa_code}>'