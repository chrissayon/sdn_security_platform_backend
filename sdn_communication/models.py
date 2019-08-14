from django.db import models

class SwitchHardware(models.Model):
    '''Model for hardware description'''
    dp_desc = models.CharField(default = "", max_length = 50)
    mfr_desc = models.CharField(default = "", max_length = 50)
    hw_desc = models.CharField(default = "", max_length = 50)
    sw_desc = models.CharField(default = "", max_length = 50)
    serial_num = models.CharField(default = "", max_length = 50)
    dp_desc= models.CharField(default = "", max_length = 50)


# # Create your models here.
class Switch(models.Model):
    switch_number = models.IntegerField(default=0)
    switch_id = models.IntegerField(default=0)
