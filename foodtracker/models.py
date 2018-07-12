# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    phone = models.CharField(max_length=10)
    adhaar_no = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    category = models.CharField(max_length=200)

class NGO(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField()
    phone = models.CharField(max_length=200)
    location=models.CharField(max_length=200)

class leaderBoard(models.Model):
    area_name = models.CharField(max_length=200)
    points = models.IntegerField()
    rank = models.IntegerField()

class DonorData(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    description = models.CharField(max_length=200)

