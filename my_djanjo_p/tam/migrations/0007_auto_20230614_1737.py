# Generated by Django 3.2.19 on 2023-06-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0006_remove_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='table_number',
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_number',
        ),
        migrations.AddField(
            model_name='book',
            name='reservt',
            field=models.DecimalField(decimal_places=0, default=10, max_digits=2),
        ),
    ]
