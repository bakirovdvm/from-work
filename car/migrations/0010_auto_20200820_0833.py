# Generated by Django 3.0.8 on 2020-08-20 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20200819_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Car'),
        ),
    ]
