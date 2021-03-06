# Generated by Django 3.0.8 on 2020-08-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.RemoveField(
            model_name='car',
            name='lenght',
        ),
        migrations.AddField(
            model_name='car',
            name='length',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='clearance',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='height',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_auto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='name_auto',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='width',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(),
        ),
    ]
