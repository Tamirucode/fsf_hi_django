from django.db import models

# Create your models here.


class Table(models.Model):
    table_name = models.CharField(max_length=20)
    table_number = models.DecimalField(decimal_places=0, max_digits=2)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    
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
    BOOKED = 'B'
    CANCELLED = 'C'

    TABLE_STATUSES = ((BOOKED, 'Booked'),
                      (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=20)
    user_id = models.DecimalField(decimal_places=0, max_digits=2)
    table_id = models.DecimalField(decimal_places=0, max_digits=2)
    table_name = models.CharField(max_length=20)
    table_number = models.DecimalField(decimal_places=0, max_digits=2)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TABLE_STATUSES,
                              default=CANCELLED, max_length=2)

    def __str__(self):
        return self.email