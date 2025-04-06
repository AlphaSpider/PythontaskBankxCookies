from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length=250)
    uname=models.CharField(max_length=100)
    pswd=models.CharField(max_length=100)
    adrs=models.CharField(max_length=250)
    ph=models.CharField(max_length=10)
    bal=models.FloatField()
    class Meta:
        db_table="account_tbl"