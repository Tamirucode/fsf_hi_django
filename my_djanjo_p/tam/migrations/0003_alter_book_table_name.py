# Generated by Django 3.2.19 on 2023-06-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0002_auto_20230612_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='table_name',
            field=models.CharField(max_length=20),
        ),
    ]
