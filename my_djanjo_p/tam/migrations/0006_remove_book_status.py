# Generated by Django 3.2.19 on 2023-06-14 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0005_table_reservt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
    ]
