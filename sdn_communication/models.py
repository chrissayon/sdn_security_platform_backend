from django.db import models

# # Create your models here.
class Switch(models.Model):
    switch_number = models.IntegerField(default=0)
    switch_id = models.IntegerField(default=0)
