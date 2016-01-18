# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=8)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=8)),
                ('address_full', models.CharField(max_length=400)),
                ('house_number', models.IntegerField()),
                ('country', models.CharField(max_length=300)),
                ('region', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('floorspace', models.IntegerField()),
                ('people', models.IntegerField()),
                ('cost', models.DecimalField(max_digits=12, decimal_places=2)),
                ('floorlevel', models.IntegerField()),
                ('lift', models.BooleanField()),
                ('garden', models.BooleanField()),
                ('parking', models.BooleanField()),
                ('kitchen', models.BooleanField()),
                ('bathroom', models.BooleanField()),
                ('bath', models.BooleanField()),
                ('shower', models.BooleanField()),
                ('floorheating', models.BooleanField()),
                ('aircon', models.BooleanField()),
                ('washmachine', models.BooleanField()),
                ('pets', models.BooleanField()),
                ('television', models.BooleanField()),
                ('catering', models.BooleanField()),
                ('disabled', models.BooleanField()),
                ('swimmingpool', models.BooleanField()),
                ('interenet', models.BooleanField()),
                ('picturesurl', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBooking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrivaldate', models.DateField()),
                ('departuredate', models.DateField()),
                ('rate', models.DecimalField(max_digits=12, decimal_places=2)),
                ('people', models.IntegerField()),
                ('identity', models.CharField(max_length=20)),
                ('confirmed', models.BooleanField()),
                ('client', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(to='homes.Room')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='room',
            field=models.ForeignKey(to='homes.Room'),
        ),
    ]
