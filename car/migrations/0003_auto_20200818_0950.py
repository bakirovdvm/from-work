# Generated by Django 3.0.8 on 2020-08-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20200818_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='engine_capacity',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(default='autom', max_length=50),
        ),
    ]
