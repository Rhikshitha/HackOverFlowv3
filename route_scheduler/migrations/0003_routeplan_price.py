# Generated by Django 4.2.7 on 2023-11-05 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route_scheduler', '0002_remove_routeplan_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeplan',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
