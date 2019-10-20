# Generated by Django 2.2.1 on 2019-10-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0030_auto_20191021_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationmodel',
            name='flow_aggregate_difference_threshold',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='configurationmodel',
            name='flow_aggregate_threshold',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='configurationmodel',
            name='port_diff_threshold',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='configurationmodel',
            name='port_threshold',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatediffstats',
            name='api_retry',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatediffstats',
            name='byte_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatediffstats',
            name='dpid',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatediffstats',
            name='flow_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatediffstats',
            name='packet_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatestats',
            name='byte_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatestats',
            name='dpid',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatestats',
            name='flow_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowaggregatestats',
            name='packet_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='byte_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='cookie',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='dpid',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='duration_nsec',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='duration_sec',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='flags',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='hard_timeout',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='idle_timeout',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='length',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='packet_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='priority',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='flowstats',
            name='table_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='api_retry',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='collisions',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='dpid',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='duration_nsec',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='duration_sec',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='rx_bytes',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='rx_crc_err',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='rx_dropped',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='rx_errors',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='rx_frame_err',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='rx_over_err',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='rx_packets',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='tx_bytes',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='tx_dropped',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='tx_errors',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portdiffstats',
            name='tx_packets',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='collisions',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='dpid',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='duration_nsec',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='duration_sec',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='rx_bytes',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='rx_crc_err',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='rx_dropped',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='rx_errors',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='rx_frame_err',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='rx_over_err',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='rx_packets',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='tx_bytes',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='tx_dropped',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='tx_errors',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='portstats',
            name='tx_packets',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='switch',
            name='switch_number',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='tablestats',
            name='active_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='tablestats',
            name='dpid',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='tablestats',
            name='lookup_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='tablestats',
            name='matched_count',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='tablestats',
            name='table_id',
            field=models.BigIntegerField(default=-1),
        ),
    ]