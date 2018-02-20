# Generated by Django 2.0.2 on 2018-02-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydives_api', '0002_locationinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationinfo',
            name='LocType',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='locationinfo',
            name='details',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='locationinfo',
            name='latitude',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='locationinfo',
            name='location',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='locationinfo',
            name='longitude',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]