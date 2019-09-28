from celery import task
from celery import shared_task
from rest_framework import status
import requests
import tensorflow as tf
import numpy as np
import time
import datetime

from .models import Switch, DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats
from .models import FlowAggregateDiffStats, PortDiffStats, AttackNotification, ConfigurationModel

def get_switch_number():
    '''Check the amount of switches in the network'''
    response = requests.get('http://0.0.0.0:8080/stats/switches')
    return response

def get_switch_desc():
    '''Check the switch desciption'''
    switch_instance = Switch.objects.get(id = 1)
    response = requests.get('http://0.0.0.0:8080/stats/desc/' + str(switch_instance.switch_number))
    return response

def get_flow_stats():
    '''Check the flow stats in the network'''
    switch_instance = Switch.objects.get(id = 1)
    # response = requests.get('http://0.0.0.0:8080/stats/flow/1')
    response = requests.get('http://0.0.0.0:8080/stats/flow/' + str(switch_instance.switch_number))
    return response

def get_agg_flow_stats():
    '''Check the aggregate flow stats on the switch'''
    switch_instance = Switch.objects.get(id = 1)
    # response = requests.get('http://0.0.0.0:8080/stats/aggregateflow/1')
    response = requests.get('http://0.0.0.0:8080/stats/aggregateflow/' + str(switch_instance.switch_number))
    return response

def get_port_stats():
    '''Check the port stats on the switch'''
    switch_instance = Switch.objects.get(id = 1)
    # response = requests.get('http://0.0.0.0:8080/stats/port/1')
    response = requests.get('http://0.0.0.0:8080/stats/port/' + str(switch_instance.switch_number))
    return response

def write_switch_number(response_data):
    '''Write port data to database'''
    if response_data.status_code != status.HTTP_200_OK:
        return False
    else:
        json_data = response_data.json()
        try:
            # If entry already exists in database, update it
            switch_instance = Switch.objects.get(id=1)
            switch_instance.switch_number = json_data[0]
            switch_instance.save()
        except Switch.DoesNotExist:
            # If entry doesn't exists, create a new one
            switch_desc_instance = Switch.objects.create(
                switch_number = json_data[0],
            )
        return True

def write_switch_desc(response_data):
    '''Write hardware description to database'''

    if response_data.status_code != status.HTTP_200_OK:
        return False
    else:
        json_data_full = response_data.json()
        # if len(json_data_full) == 0:
        #     return False

        json_keys = json_data_full.keys()
        dict_keys = list(json_keys)
        json_data = json_data_full[dict_keys[0]]

        # Exit if there is no data on controller response
        if len(json_data) == 0:
            return False

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

        # Exit if there is no data on controller response
        if len(json_data) == 0:
            return False

        # Cycle through all the flow entries
        # for i in range(0, max_loop):
        #     try:
        #         # If entry already exists in database, update it
        #         port_stats_instance               = PortStats.objects.get(id = i + 1)
        #         port_stats_instance.dpid          = dict_keys[0]
        #         port_stats_instance.tx_dropped    = json_data[i]["tx_dropped"]
        #         port_stats_instance.rx_packets    = json_data[i]["rx_packets"]
        #         port_stats_instance.rx_crc_err    = json_data[i]["rx_crc_err"]
        #         port_stats_instance.tx_bytes      = json_data[i]["tx_bytes"]
        #         port_stats_instance.rx_dropped    = json_data[i]["rx_dropped"]
        #         port_stats_instance.port_no       = json_data[i]["port_no"]
        #         port_stats_instance.rx_over_err   = json_data[i]["rx_over_err"]
        #         port_stats_instance.rx_frame_err  = json_data[i]["rx_frame_err"]
        #         port_stats_instance.rx_bytes      = json_data[i]["rx_bytes"]
        #         port_stats_instance.tx_errors     = json_data[i]["tx_errors"]
        #         port_stats_instance.duration_nsec = json_data[i]["duration_nsec"]
        #         port_stats_instance.collisions    = json_data[i]["collisions"]
        #         port_stats_instance.duration_sec  = json_data[i]["duration_sec"]
        #         port_stats_instance.rx_errors     = json_data[i]["rx_errors"]
        #         port_stats_instance.tx_packets    = json_data[i]["tx_packets"]
        #         port_stats_instance.save()
        #     except PortStats.DoesNotExist:
        #         # If entry doesn't exists, create a new one
        #         port_stats_instance = PortStats.objects.create(
        #             dpid          = dict_keys[0],
        #             tx_dropped    = json_data[i]["tx_dropped"],
        #             rx_packets    = json_data[i]["rx_packets"],
        #             rx_crc_err    = json_data[i]["rx_crc_err"],
        #             tx_bytes      = json_data[i]["tx_bytes"],
        #             rx_dropped    = json_data[i]["rx_dropped"],
        #             port_no       = json_data[i]["port_no"],
        #             rx_over_err   = json_data[i]["rx_over_err"],
        #             rx_frame_err  = json_data[i]["rx_frame_err"],
        #             rx_bytes      = json_data[i]["tx_bytes"],
        #             tx_errors     = json_data[i]["tx_errors"],
        #             duration_nsec = json_data[i]["duration_nsec"],
        #             collisions    = json_data[i]["collisions"],
        #             duration_sec  = json_data[i]["duration_sec"],
        #             rx_errors     = json_data[i]["rx_errors"],
        #             tx_packets    = json_data[i]["tx_packets"],
        #         )

        for i in range(0, max_loop):
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

            # print(json_data[i]["port_no"])

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

        # Exit if there is no data on controller response
        if len(json_data) == 0:
            return False


        # # Cycle through all the flow entries
        # for i in range(0, max_loop):
        #     try:
        #         # If entry already exists in database, update it
        #         flow_agg_stats_instance              = FlowAggregateStats.objects.get(id = i + 1)
        #         flow_agg_stats_instance.dpid         = dict_keys[0]
        #         flow_agg_stats_instance.packet_count = json_data[i]["packet_count"]
        #         flow_agg_stats_instance.byte_count   = json_data[i]["byte_count"]
        #         flow_agg_stats_instance.flow_count   = json_data[i]["flow_count"]
        #         flow_agg_stats_instance.save()
        #     except FlowAggregateStats.DoesNotExist:
        #         # If entry doesn't exists, create a new one
        #         flow_stats_instance = FlowAggregateStats.objects.create(
        #             dpid         = dict_keys[0],
        #             packet_count = json_data[i]["packet_count"],
        #             byte_count   = json_data[i]["byte_count"],
        #             flow_count   = json_data[i]["flow_count"],
        #         )

        for i in range(0, max_loop):
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

        # Exit if there is no data on controller response
        if len(json_data) == 0:
            return False

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
                # print(flow_stats_instance.last_modified)
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

def write_flow_agg_diff_stats():
    '''Write flow statistics to database'''
    flow_agg_stats = FlowAggregateStats.objects.all()
    length_flow_agg = len(flow_agg_stats)

    # Check if there are at least two entries
    if(length_flow_agg <= 1):
        return False

    # Obtain last and second last entry
    latest_flow_agg_stats = flow_agg_stats[length_flow_agg - 1]
    penultimate_flow_agg_stats = flow_agg_stats[length_flow_agg - 2]

    diff_packet_count = latest_flow_agg_stats.packet_count - penultimate_flow_agg_stats.packet_count
    diff_byte_count   = latest_flow_agg_stats.byte_count - penultimate_flow_agg_stats.byte_count
    diff_flow_count   = latest_flow_agg_stats.flow_count - penultimate_flow_agg_stats.flow_count

    # If negative entry
    if(diff_packet_count < 0):
        return False
    elif((diff_byte_count < 0) | (diff_byte_count > 1000000000000)):
        return False

    flow_agg_stats_diff_instance = FlowAggregateDiffStats.objects.create(
        packet_count     = diff_packet_count,
        byte_count       = diff_byte_count,
        flow_count       = diff_flow_count,
        time_interval    = latest_flow_agg_stats.created.timestamp() - penultimate_flow_agg_stats.created.timestamp(),
        api_retry        = -1,
        latest_flow_fk   = latest_flow_agg_stats,
        penultimate_flow_fk = penultimate_flow_agg_stats,
    )
    #print(length_flow_agg)
    # print(flow_agg_stats[length_flow_agg - 1])
    flow_agg_stats_diff_instance.save()

    return True

def write_port_diff_stats(port):
    '''Write flow statistics to database'''
    port_stats = PortStats.objects.filter(port_no = port)

    length_port = len(port_stats)

    # Check if there are at least two entries
    if(length_port <= 1):
        return False

    # Obtain last and second last entry
    latest_port_stats = port_stats[length_port - 1]
    penultimate_port_stats = port_stats[length_port - 2]
    port_stats_instance = PortDiffStats.objects.create(
        tx_dropped    = latest_port_stats.tx_dropped    - penultimate_port_stats.tx_dropped,
        rx_packets    = latest_port_stats.rx_packets    - penultimate_port_stats.rx_packets,
        rx_crc_err    = latest_port_stats.rx_crc_err    - penultimate_port_stats.rx_crc_err,
        tx_bytes      = latest_port_stats.tx_bytes      - penultimate_port_stats.tx_bytes,
        rx_dropped    = latest_port_stats.rx_dropped    - penultimate_port_stats.rx_dropped,
        port_no       = latest_port_stats.port_no,
        rx_over_err   = latest_port_stats.rx_over_err   - penultimate_port_stats.rx_over_err,
        rx_frame_err  = latest_port_stats.rx_frame_err  - penultimate_port_stats.rx_frame_err,
        rx_bytes      = latest_port_stats.rx_bytes      - penultimate_port_stats.rx_bytes,
        tx_errors     = latest_port_stats.tx_errors     - penultimate_port_stats.tx_errors,
        duration_nsec = latest_port_stats.duration_nsec - penultimate_port_stats.duration_nsec,
        collisions    = latest_port_stats.collisions    - penultimate_port_stats.collisions,
        duration_sec  = latest_port_stats.duration_sec  - penultimate_port_stats.duration_sec,
        rx_errors     = latest_port_stats.rx_errors     - penultimate_port_stats.rx_errors,
        tx_packets    = latest_port_stats.tx_packets    - penultimate_port_stats.tx_packets,
        latest_port_fk      = latest_port_stats,
        penultimate_port_fk = penultimate_port_stats
    )

    port_stats_instance.save()

    return True

def flow_aggregate_difference_threshold():
    '''Check if flow aggregate difference is bigger than threshold'''
    # Get flow aggregate stats
    flow_agg_diff_stats = FlowAggregateDiffStats.objects.last()
    byte_count = flow_agg_diff_stats.byte_count
    
    # Get threshold
    configuration_instance = ConfigurationModel.objects.get(id = 1)
    byte_count_threshold = configuration_instance.flow_aggregate_threshold
    
    attack_true = byte_count > byte_count_threshold

    if (attack_true):
        attack_notification = AttackNotification.objects.create(
            attack_type   = "Denial of Service", #DDoS, controller comprmise, etc
            attack_vector = "Flow Aggregate Difference", #Where the attack came from (flow_aggregate, port statistics)
            percentage    = -1, # Percentage of the value from the machine learning model
            threshold     = byte_count_threshold, # Threshold for value to be considered valid
            attack_true   = attack_true # Attack is valid when percentage > threshold
        )
        return True
    else:
        return False

def ml_flow_agg_diff_stats(threshold):
    model = tf.keras.models.load_model('my_model.h5')
    flow_agg_diff_stats = FlowAggregateDiffStats.objects.last()
    # print(flow_agg_diff_stats.packet_count)
    # time.sleep(5)
    network_data = np.array([[
        flow_agg_diff_stats.packet_count,
        flow_agg_diff_stats.byte_count,
        flow_agg_diff_stats.time_interval,
        0
    ]])
    result = model.predict(network_data)
    # print(result[0][0])

    attack_true = (result[0][0] > threshold)
    # print(attack_true)

    if (attack_true):
        attack_notification = AttackNotification.objects.create(
            attack_type   = "Denial of Service", #DDoS, controller comprmise, etc
            attack_vector = "Flow Aggregate", #Where the attack came from (flow_aggregate, port statistics)
            percentage    = result[0][0], # Percentage of the value from the machine learning model
            threshold     = threshold, # Threshold for value to be considered valid
            attack_true   = attack_true # Attack is valid when percentage > threshold
        )

    # print(attack_notification.attack_type)
    # print(attack_notification.attack_vector)
    # print(attack_notification.percentage)
    # print(attack_notification.threshold)
    # print(attack_notification.attack_true)
    # print(datetime.datetime.now().timestamp() - flow_agg_diff_stats.created.timestamp())
    # print(flow_agg_diff_stats.time_interval)
    # # print("\n")
    # print(result)
    return True


# @task(name='summary')
# def sdn_data_retreieval():
#     switch_number = get_switch_number()
#     write_switch_number(switch_number)

#     # Hardware description
#     switch_desc = get_switch_desc()
#     switch_desc_result = write_switch_desc(switch_desc)

#     # FLow stats
#     flow_stats = get_flow_stats()
#     flow_stats_result = write_flow_stats(flow_stats)

#     # Flow Aggregate stats
#     agg_flow_stats = get_agg_flow_stats()
#     agg_flow_stats_result = write_agg_flow_stats(agg_flow_stats)

#     # Port Stats
#     port_stats = get_port_stats()
#     port_stats_result = write_port_stats(port_stats)

#     # Flow Aggregate Stats difference
#     flow_agg_diff_stats = write_flow_agg_diff_stats()

#     # Port stat difference
#     write_port_diff_stats(1)
#     write_port_diff_stats(2)
#     write_port_diff_stats(3)
#     write_port_diff_stats('LOCAL')

#     # # Run port data through classifier
#     ml_flow_agg_diff_stats(0)
#     # t0 = time.time()
#     time.sleep(5)
#     # t1 = time.time()

@task(name='summary')
def sdn_data_retreieval():
    flow_aggregate_difference_threshold
    time.sleep(5)
    