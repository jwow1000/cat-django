# Generated by Django 5.0.3 on 2024-04-04 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding Date'),
        ),
    ]