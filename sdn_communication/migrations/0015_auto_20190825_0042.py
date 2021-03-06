# Generated by Django 2.2.1 on 2019-08-24 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0014_auto_20190824_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowaggregatediffstats',
            name='latest_flow_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='latest', to='sdn_communication.FlowAggregateStats'),
        ),
        migrations.AddField(
            model_name='flowaggregatediffstats',
            name='penultimate_flow_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='penultimate', to='sdn_communication.FlowAggregateStats'),
        ),
    ]
