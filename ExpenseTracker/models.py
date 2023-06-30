from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=60,blank=False,default='')
    email = models.CharField(max_length=60,blank=False,default='')
    phone = models.CharField(max_length=60,blank=False,default='')
    password = models.CharField(max_length=60,blank=False,default='')
    city = models.CharField(max_length=60,blank=False,default='')
    Balance = models.CharField(max_length=60,blank=False,default='')
    date = models.CharField(max_length=60,blank=False,default='')
    time = models.CharField(max_length=60,blank=False,default='')
    Limit = models.CharField(max_length=60,blank=False,default='')
    Proffesion = models.CharField(max_length=60,blank=False,default='')
    Age = models.CharField(max_length=60,blank=False,default='')

class Expense(models.Model):
    Amount = models.CharField(max_length=60,blank=False,default='')
    where = models.CharField(max_length=60,blank=False,default='')
    Why = models.CharField(max_length=60,blank=False,default='')
    date_day = models.CharField(max_length=60,blank=False,default='')
    date_month = models.CharField(max_length=60,blank=False,default='')
    date_year = models.CharField(max_length=60,blank=False,default='')
    time = models.CharField(max_length=60,blank=False,default='')
    category = models.CharField(max_length=60,blank=False,default='')
    wasitneeded = models.CharField(max_length=60,blank=False,default='')

    