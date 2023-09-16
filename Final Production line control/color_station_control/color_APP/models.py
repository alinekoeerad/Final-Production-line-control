import datetime

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django_jalali.db import models as jmodels


class Station(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse("stations")


class Fault(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse("faults")


class Report(models.Model):
    fault = models.ForeignKey('Fault', blank=True, on_delete=models.SET_NULL, null=True)
    station = models.ForeignKey('Station', on_delete=models.SET_NULL, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    shift = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], null=True, blank=True)
    reporter = models.CharField(max_length=100, null=True, blank=True)
    expert = models.CharField(max_length=100, null=True, blank=True)
    opinion = models.TextField(null=True, blank=True)
    piece = models.ManyToManyField('Piece', blank=True)
    date = jmodels.jDateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    stopTime = models.TimeField(blank=True)
    samp = models.URLField(null=True, blank=True)
    cReport = models.TextField(null=True, blank=True)
    equip = models.ForeignKey('Equip', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.fault) + " " + str(self.station)


class Equip(models.Model):
    name = models.CharField(max_length=100)
    station = models.ForeignKey('Station', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Report)
def calcStopTime(sender, instance, **kwargs):
    end = str(instance.endTime).split(':')
    start = str(instance.startTime).split(':')
    instance.stopTime = str(
        datetime.timedelta(hours=int(end[0]), minutes=int(end[1]), seconds=int(end[2])) - datetime.timedelta(
            hours=int(start[0]), minutes=int(start[1]), seconds=int(start[2])))


class Piece(models.Model):
    name = models.CharField(max_length=100)
    ikco_id = models.CharField(max_length=100)
    technical_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name
