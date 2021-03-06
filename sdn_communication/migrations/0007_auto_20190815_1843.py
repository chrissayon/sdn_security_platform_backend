# Generated by Django 2.2.1 on 2019-08-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0006_remove_switchhardware_dpid'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mfr_desc', models.CharField(default='', max_length=50)),
                ('hw_desc', models.CharField(default='', max_length=50)),
                ('sw_desc', models.CharField(default='', max_length=50)),
                ('serial_num', models.CharField(default='', max_length=50)),
                ('dp_desc', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FlowAggregateStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpid', models.IntegerField(default=0)),
                ('packet_count', models.IntegerField(default=0)),
                ('byte_count', models.IntegerField(default=0)),
                ('flow_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FlowStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpid', models.IntegerField(default=0)),
                ('idle_timeout', models.IntegerField(default=0)),
                ('cookie', models.IntegerField(default=0)),
                ('packet_count', models.IntegerField(default=0)),
                ('hard_timeout', models.IntegerField(default=0)),
                ('byte_count', models.IntegerField(default=0)),
                ('duration_sec', models.IntegerField(default=0)),
                ('duration_nsec', models.IntegerField(default=0)),
                ('priority', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('flags', models.IntegerField(default=0)),
                ('table_id', models.IntegerField(default=0)),
                ('actions', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PortStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_number', models.IntegerField(default=0)),
                ('rx_packets', models.IntegerField(default=0)),
                ('rx_crc_err', models.IntegerField(default=0)),
                ('tx_bytes', models.IntegerField(default=0)),
                ('rx_dropped', models.IntegerField(default=0)),
                ('port_no', models.CharField(default='', max_length=50)),
                ('rx_over_err', models.IntegerField(default=0)),
                ('rx_frame_err', models.IntegerField(default=0)),
                ('rx_bytes', models.IntegerField(default=0)),
                ('tx_errors', models.IntegerField(default=0)),
                ('duration_nsec', models.IntegerField(default=0)),
                ('collisions', models.IntegerField(default=0)),
                ('duration_sec', models.IntegerField(default=0)),
                ('rx_errors', models.IntegerField(default=0)),
                ('tx_packets', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TableStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpid', models.IntegerField(default=0)),
                ('table_id', models.IntegerField(default=0)),
                ('matched_count', models.IntegerField(default=0)),
                ('lookup_count', models.IntegerField(default=0)),
                ('active_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='SwitchHardware',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='switch_id',
        ),
    ]
