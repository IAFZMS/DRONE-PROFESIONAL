# Generated by Django 2.2.7 on 2019-11-23 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0003_auto_20191123_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='dron',
            name='autonomia',
            field=models.CharField(default='', max_length=400),
        ),
    ]