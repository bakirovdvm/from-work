# Generated by Django 3.0.8 on 2020-08-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20200819_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default='', upload_to='car_images/'),
        ),
    ]