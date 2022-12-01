from django.db import models

# Create your models here.

class Reading(models.Model):
    reading_date = models.DateField(auto_now_add=True, verbose_name='Date')
    reading_time = models.TimeField(auto_now_add=True, verbose_name='Time')
    motorist_first_name = models.CharField(max_length=255, verbose_name='Motorist First Name')
    motorist_middle_initial = models.CharField(max_length=2, blank=True, verbose_name='Motorist Middle Initial')
    motorist_last_name = models.CharField(max_length=255, verbose_name='Motorist Last Name')
    plate_number = models.CharField(max_length=20, verbose_name='Plate No.')
    db_reading = models.IntegerField(verbose_name='dB')
    distance_reading = models.IntegerField(verbose_name='Distance')
