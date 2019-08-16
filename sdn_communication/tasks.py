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
    '''Write to database hardware description column'''
    
    if response_data.status_code != status.HTTP_200_OK:
        return False    
    else:
        json_data_full = response_data.json()
        json_keys = json_data_full.keys()
        dict_keys = list(json_keys)
        json_data = json_data_full[dict_keys[0]]
        # print(json_data)

        try:
            desc_stats_instance            = DescStats.objects.get(id=1)
            desc_stats_instance.dp_desc    = json_data["dp_desc"],
            desc_stats_instance.mfr_desc   = json_data["mfr_desc"],
            desc_stats_instance.hw_desc    = json_data["hw_desc"],
            desc_stats_instance.sw_desc    = json_data["sw_desc"],
            desc_stats_instance.serial_num = json_data["serial_num"],
        except DescStats.DoesNotExist:
            switch_desc_instance = DescStats.objects.create(
                dp_desc    = json_data["dp_desc"],
                mfr_desc   = json_data["mfr_desc"],
                hw_desc    = json_data["hw_desc"],
                sw_desc    = json_data["sw_desc"],
                serial_num = json_data["serial_num"],
            )

        return True

def write_flow_stats(response_data):
    '''Write to database hardware description column'''
    
    if response_data.status_code != status.HTTP_200_OK:
        return False    
    else:
        json_data_full = response_data.json()
        json_keys = json_data_full.keys()
        dict_keys = list(json_keys)
        json_data = json_data_full[dict_keys[0]]
        #print(json_data[0]["actions"])

        
        flow_stats_instance = FlowStats.objects.create(
                dpid          = dict_keys[0],
                actions       = json_data[0]["actions"],
                idle_timeout  = json_data[0]["idle_timeout"],
                cookie        = json_data[0]["cookie"],
                packet_count  = json_data[0]["packet_count"],
                hard_timeout  = json_data[0]["hard_timeout"],
                byte_count    = json_data[0]["byte_count"],
                duration_sec  = json_data[0]["duration_sec"],
                duration_nsec = json_data[0]["duration_nsec"],
                priority      = json_data[0]["priority"],
                length        = json_data[0]["length"],
                flags         = json_data[0]["flags"],
                table_id      = json_data[0]["table_id"],
        )

        return True


@task(name='summary')
def sdn_data_retreieval():
    switch_desc = get_switch_desc()
    test = write_switch_desc(switch_desc)