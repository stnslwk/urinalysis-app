# Generated by Django 2.0.2 on 2018-03-11 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20180311_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substance',
            name='record_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Time'),
        ),
    ]