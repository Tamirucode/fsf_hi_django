from django.db import models

# Create your models here.


class Table(models.Model):
    table_name = models.CharField(max_length=20)
    reservt = models.DecimalField(decimal_places=0, max_digits=2)
    booked_table = models.DecimalField(decimal_places=0, max_digits=2)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.table_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Book(models.Model):
    
    email = models.EmailField()
    name = models.CharField(max_length=20)
    userid = models.DecimalField(decimal_places=0, max_digits=2)
    tableid = models.DecimalField(decimal_places=0, max_digits=2)
    table_name = models.CharField(max_length=20)
    booked_table = models.DecimalField(decimal_places=0, max_digits=2)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.email
