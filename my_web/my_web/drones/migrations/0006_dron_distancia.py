# Generated by Django 2.2.7 on 2019-11-23 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0005_auto_20191123_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='dron',
            name='distancia',
            field=models.CharField(default='', max_length=400),
        ),
    ]
