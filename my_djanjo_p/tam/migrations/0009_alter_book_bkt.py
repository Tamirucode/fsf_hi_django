# Generated by Django 3.2.19 on 2023-06-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0008_auto_20230614_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bkt',
            field=models.DecimalField(decimal_places=0, default=10, max_digits=2),
        ),
    ]