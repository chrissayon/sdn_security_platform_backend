# # Create your tasks here
# from __future__ import absolute_import, unicode_literals

from celery import task
from celery import shared_task
from rest_framework import status
import requests

from .models import Switch, SwitchHardware

def get_switch_number():
    #Check the amount of switches in the network
    response = requests.get('http://0.0.0.0:8080/stats/switches')

    if response.status_code != status.HTTP_200_OK:
        return response.status_code

    return response

def get_switch_desc():
    #Check the switch desciption
    response = requests.get('http://0.0.0.0:8080/stats/desc/1')

    if response.status_code != status.HTTP_200_OK:
        return response.status_code

    return response

def get_flow_stats():
    #Check the flow stats in the network
    response = requests.get('http://0.0.0.0:8080/stats/flow/1')

    if response.status_code != status.HTTP_200_OK:
        return response.status_code

    return response

def get_agg_flow_stats():
    #Check the aggregate flow stats on the switch
    response = requests.get('http://0.0.0.0:8080/stats/aggregateflow/1')

    if response.status_code != status.HTTP_200_OK:
        return response.status_code

    return response

def get_port_stats():
    #Check the port stats on the switch
    response = requests.get('http://0.0.0.0:8080/stats/port/1/1')

    if response.status_code != status.HTTP_200_OK:
        return response.status_code

    return response

def write_to_db(json_data, table):
    pass

@task(name='summary')
def sdn_data_retreieval():
    switch_desc = get_switch_desc()
    switch_desc = switch_desc.json()
    print(switch_desc['1'])

    # Get keys from list
    json_keys = switch_desc.keys()

    # Turn into a list
    dict_keys = list(json_keys)

    # Use first parameter from list as key on JSON object
    description = switch_desc[dict_keys[0]]

    switch_instance = SwitchHardware.objects.create(
            #dp_desc = description["dp_desc"],
            mfr_desc = description["mfr_desc"],
            hw_desc = description["hw_desc"],
            sw_desc = description["sw_desc"],
            serial_num = description["serial_num"],
            dp_desc = description["dp_desc"],
    )



    print(description)

    # print(switch_desc



    #switch_instance = Switch.objects.create(switch_number = json_response["1"][2]["rx_packets"])
    #switch_instance = Switch.objects.create(switch_id=json_response["1"][2]["rx_packets"])
