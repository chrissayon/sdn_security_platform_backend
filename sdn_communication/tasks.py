from celery import task
from celery import shared_task
from rest_framework import status
import requests

from .models import DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats

def get_switch_number():
    '''Check the amount of switches in the network'''
    response = requests.get('http://0.0.0.0:8080/stats/switches')
    return response

def get_switch_desc():
    '''Check the switch desciption'''
    response = requests.get('http://0.0.0.0:8080/stats/desc/1')
    return response

def get_flow_stats():
    '''Check the flow stats in the network'''
    response = requests.get('http://0.0.0.0:8080/stats/flow/1')
    return response

def get_agg_flow_stats():
    '''Check the aggregate flow stats on the switch'''
    response = requests.get('http://0.0.0.0:8080/stats/aggregateflow/1')
    return response

def get_port_stats():
    '''Check the port stats on the switch'''
    response = requests.get('http://0.0.0.0:8080/stats/port/1/1')
    return response

def write_switch_number(json_data):
    pass

def write_switch_desc(response_data):
    '''Write hardware description to database'''

    if response_data.status_code != status.HTTP_200_OK:
        return False
    else:
        json_data_full = response_data.json()
        json_keys = json_data_full.keys()
        dict_keys = list(json_keys)
        json_data = json_data_full[dict_keys[0]]
        # print(json_data)

        try:
            # If entry already exists in database, update it
            desc_stats_instance            = DescStats.objects.get(id=1)
            desc_stats_instance.dp_desc    = json_data["dp_desc"],
            desc_stats_instance.mfr_desc   = json_data["mfr_desc"],
            desc_stats_instance.hw_desc    = json_data["hw_desc"],
            desc_stats_instance.sw_desc    = json_data["sw_desc"],
            desc_stats_instance.serial_num = json_data["serial_num"],
            desc_stats_instance.save()
        except DescStats.DoesNotExist:
            # If entry doesn't exists, create a new one
            switch_desc_instance = DescStats.objects.create(
                dp_desc    = json_data["dp_desc"],
                mfr_desc   = json_data["mfr_desc"],
                hw_desc    = json_data["hw_desc"],
                sw_desc    = json_data["sw_desc"],
                serial_num = json_data["serial_num"],
            )

        return True

def write_port_stats(response_data):
    '''Write port statistics to database'''

    if response_data.status_code != status.HTTP_200_OK:
        return False
    else:
        json_data_full = response_data.json()
        json_keys = json_data_full.keys()
        dict_keys = list(json_keys)
        json_data = json_data_full[dict_keys[0]]
        max_loop = len(json_data)

        # Cycle through all the flow entries
        for i in range(0, max_loop):
            try:
                # If entry already exists in database, update it
                port_stats_instance               = PortStats.objects.get(id = i + 1)
                port_stats_instance.dpid          = dict_keys[0]
                port_stats_instance.tx_dropped    = json_data[i]["tx_dropped"]
                port_stats_instance.rx_packets    = json_data[i]["rx_packets"]
                port_stats_instance.ex_crc_err    = json_data[i]["ex_crc_err"]
                port_stats_instance.tx_bytes      = json_data[i]["tx_bytes"]
                port_stats_instance.rx_dropped    = json_data[i]["rx_dropped"]
                port_stats_instance.port_no       = json_data[i]["port_no"]
                port_stats_instance.rx_over_err   = json_data[i]["rx_over_err"]
                port_stats_instance.rx_frame_err  = json_data[i]["rx_frame_err"]
                port_stats_instance.rx_bytes      = json_data[i]["rx_bytes"]
                port_stats_instance.tx_errors     = json_data[i]["tx_erros"]
                port_stats_instance.duration_nsec = json_data[i]["duration_nsec"]
                port_stats_instance.collisions    = json_data[i]["collisions"]
                port_stats_instance.duration_sec  = json_data[i]["duration_sec"]
                port_stats_instance.rx_errors     = json_data[i]["rx_errors"]
                port_stats_instance.tx_packets    = json_data[i]["tx_packets"]
                port_stats_instance.save()
            except PortStats.DoesNotExist:
                # If entry doesn't exists, create a new one
                port_stats_instance = PortStats.objects.create(
                    dpid          = dict_keys[0],
                    tx_dropped    = json_data[i]["tx_dropped"],
                    rx_packets    = json_data[i]["rx_packets"],
                    rx_crc_err    = json_data[i]["rx_crc_err"],
                    tx_bytes      = json_data[i]["tx_bytes"],
                    rx_dropped    = json_data[i]["rx_dropped"],
                    port_no       = json_data[i]["port_no"],
                    rx_over_err   = json_data[i]["rx_over_err"],
                    rx_frame_err  = json_data[i]["rx_frame_err"],
                    rx_bytes      = json_data[i]["tx_bytes"],
                    tx_errors     = json_data[i]["tx_errors"],
                    duration_nsec = json_data[i]["duration_nsec"],
                    collisions    = json_data[i]["collisions"],
                    duration_sec  = json_data[i]["duration_sec"],
                    rx_errors     = json_data[i]["rx_errors"],
                    tx_packets    = json_data[i]["tx_packets"],
                )

        return True


def write_agg_flow_stats(response_data):
    '''Write aggregate flow statistics to database'''

    if response_data.status_code != status.HTTP_200_OK:
        return False
    else:
        json_data_full = response_data.json()
        json_keys = json_data_full.keys()
        dict_keys = list(json_keys)
        json_data = json_data_full[dict_keys[0]]
        max_loop = len(json_data)

        # Cycle through all the flow entries
        for i in range(0, max_loop):
            try:
                # If entry already exists in database, update it
                flow_agg_stats_instance              = FlowAggregateStats.objects.get(id = i + 1)
                flow_agg_stats_instance.dpid         = dict_keys[0]
                flow_agg_stats_instance.packet_count = json_data[i]["packet_count"]
                flow_agg_stats_instance.byte_count   = json_data[i]["byte_count"]
                flow_agg_stats_instance.flow_count   = json_data[i]["flow_count"]
                flow_agg_stats_instance.save()
            except FlowAggregateStats.DoesNotExist:
                # If entry doesn't exists, create a new one
                flow_stats_instance = FlowAggregateStats.objects.create(
                    dpid         = dict_keys[0],
                    packet_count = json_data[i]["packet_count"],
                    byte_count   = json_data[i]["byte_count"],
                    flow_count   = json_data[i]["flow_count"],
                )

        return True

def write_flow_stats(response_data):
    '''Write flow statistics to database'''

    if response_data.status_code != status.HTTP_200_OK:
        return False
    else:
        json_data_full = response_data.json()
        json_keys = json_data_full.keys()
        dict_keys = list(json_keys)
        json_data = json_data_full[dict_keys[0]]
        max_loop = len(json_data)

        # Cycle through all the flow entries
        for i in range(0, max_loop):
            try:
                # If entry already exists in database, update it
                flow_stats_instance               = FlowStats.objects.get(id = i + 1)
                flow_stats_instance.dpid          = dict_keys[0]
                flow_stats_instance.actions       = json_data[i]["actions"]
                flow_stats_instance.idle_timeout  = json_data[i]["idle_timeout"]
                flow_stats_instance.cookie        = json_data[i]["cookie"]
                flow_stats_instance.packet_count  = json_data[i]["packet_count"]
                flow_stats_instance.hard_timeout  = json_data[i]["hard_timeout"]
                flow_stats_instance.byte_count    = json_data[i]["byte_count"]
                flow_stats_instance.duration_sec  = json_data[i]["duration_sec"]
                flow_stats_instance.duration_nsec = json_data[i]["duration_nsec"]
                flow_stats_instance.priority      = json_data[i]["priority"]
                flow_stats_instance.length        = json_data[i]["length"]
                flow_stats_instance.flags         = json_data[i]["flags"]
                flow_stats_instance.table_id      = json_data[i]["table_id"]
                flow_stats_instance.match         = json_data[i]["match"]
                flow_stats_instance.save()
            except FlowStats.DoesNotExist:
                # If entry doesn't exists, create a new one
                flow_stats_instance = FlowStats.objects.create(
                    dpid          = dict_keys[0],
                    actions       = json_data[i]["actions"],
                    idle_timeout  = json_data[i]["idle_timeout"],
                    cookie        = json_data[i]["cookie"],
                    packet_count  = json_data[i]["packet_count"],
                    hard_timeout  = json_data[i]["hard_timeout"],
                    byte_count    = json_data[i]["byte_count"],
                    duration_sec  = json_data[i]["duration_sec"],
                    duration_nsec = json_data[i]["duration_nsec"],
                    priority      = json_data[i]["priority"],
                    length        = json_data[i]["length"],
                    flags         = json_data[i]["flags"],
                    table_id      = json_data[i]["table_id"],
                    match         = json_data[i]["match"],
                )

        return True


@task(name='summary')
def sdn_data_retreieval():
    switch_desc = get_switch_desc()
    switch_desc_result = write_switch_desc(switch_desc)

    flow_stats = get_flow_stats()
    flow_stat_result = write_flow_stats(flow_stats)
