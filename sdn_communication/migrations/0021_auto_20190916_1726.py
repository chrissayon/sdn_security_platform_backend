# Generated by Django 2.2.1 on 2019-09-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0020_auto_20190916_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flowaggregatediffstats',
            old_name='time_difference',
            new_name='interval_diff',
        ),
        migrations.AddField(
            model_name='portdiffstats',
            name='api_retry',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='portdiffstats',
            name='interval_diff',
            field=models.FloatField(default=-1),
        ),
    ]
