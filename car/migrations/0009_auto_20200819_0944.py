# Generated by Django 3.0.8 on 2020-08-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_auto_20200819_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
