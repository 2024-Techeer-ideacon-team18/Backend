from django.db import models

# Create your models here.
class mathlib(models.Model):
    math_id = models.AutoField(primary_key=True)
    math_name = models.CharField(max_length=200)

class langlib(models.Model):
    lang_id = models.AutoField(primary_key=True)
    lang_name = models.CharField(max_length=200)

class netlib(models.Model):
    net_id = models.AutoField(primary_key=True)
    net_name = models.CharField(max_length=200)

class utillib(models.Model):
    util_id = models.AutoField(primary_key=True)
    util_name = models.CharField(max_length=200)