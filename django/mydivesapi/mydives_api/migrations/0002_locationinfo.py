# Generated by Django 2.0.2 on 2018-02-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydives_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocType', models.CharField(blank=True, default='', max_length=400)),
                ('location', models.CharField(blank=True, default='', max_length=400)),
                ('latitude', models.CharField(blank=True, default='', max_length=400)),
                ('longitude', models.CharField(blank=True, default='', max_length=400)),
                ('details', models.CharField(blank=True, default='', max_length=400)),
            ],
        ),
    ]
