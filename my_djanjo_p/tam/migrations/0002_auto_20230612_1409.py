# Generated by Django 3.2.19 on 2023-06-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='rem',
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
