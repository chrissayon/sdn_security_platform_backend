# Generated by Django 2.2.1 on 2019-08-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0008_flowstats_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='portstats',
            name='dpid',
            field=models.IntegerField(default=0),
        ),
    ]
