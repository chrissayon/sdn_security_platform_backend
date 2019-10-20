from django.db import models


class DescStats(models.Model):
    '''Model for hardware description'''
    dp_desc       = models.CharField(default = "No Data Yet", max_length = 50)
    mfr_desc      = models.CharField(default = "No Data Yet", max_length = 50)
    hw_desc       = models.CharField(default = "No Data Yet", max_length = 50)
    sw_desc       = models.CharField(default = "No Data Yet", max_length = 50)
    serial_num    = models.CharField(default = "No Data Yet", max_length = 50)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class FlowStats(models.Model):
    '''Flow Table information'''
    dpid          = models.BigIntegerField(default = -1)
    actions       = models.CharField(default = "No Data Yet", max_length = 50)
    idle_timeout  = models.BigIntegerField(default = -1)
    cookie        = models.BigIntegerField(default = -1)
    packet_count  = models.BigIntegerField(default = -1)
    hard_timeout  = models.BigIntegerField(default = -1)
    byte_count    = models.CharField(default = "No Data Yet", max_length = 50)
    # byte_count    = models.BigIntegerField(default = -1)
    duration_sec  = models.BigIntegerField(default = -1)
    duration_nsec = models.BigIntegerField(default = -1)
    priority      = models.BigIntegerField(default = -1)
    length        = models.BigIntegerField(default = -1)
    flags         = models.BigIntegerField(default = -1)
    table_id      = models.BigIntegerField(default = -1)
    match         = models.CharField(default = "No Data Yet", max_length = 200)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class FlowAggregateStats(models.Model):
    '''Total amount of packets sent'''
    dpid          = models.BigIntegerField(default = -1)
    packet_count  = models.BigIntegerField(default = -1)
    byte_count    = models.BigIntegerField(default = -1)
    flow_count    = models.BigIntegerField(default = -1)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class TableStats(models.Model):
    '''Need to resolve the redundant tables that go over 100+'''
    dpid          = models.BigIntegerField(default = -1)
    table_id      = models.BigIntegerField(default = -1)
    matched_count = models.BigIntegerField(default = -1)
    lookup_count  = models.BigIntegerField(default = -1)
    active_count  = models.BigIntegerField(default = -1)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class PortStats(models.Model):
    '''Statistics on the respective port'''
    dpid          = models.BigIntegerField(default = -1)
    tx_dropped    = models.BigIntegerField(default = -1)
    # port_number   = models.BigIntegerField(default = -1)
    rx_packets    = models.BigIntegerField(default = -1)
    rx_crc_err    = models.BigIntegerField(default = -1)
    tx_bytes      = models.BigIntegerField(default = -1)
    rx_dropped    = models.BigIntegerField(default = -1)
    port_no       = models.CharField(default = "No Data Yet", max_length = 50)
    rx_over_err   = models.BigIntegerField(default = -1)
    rx_frame_err  = models.BigIntegerField(default = -1)
    rx_bytes      = models.BigIntegerField(default = -1)
    tx_errors     = models.BigIntegerField(default = -1)
    duration_nsec = models.BigIntegerField(default = -1)
    collisions    = models.BigIntegerField(default = -1)
    duration_sec  = models.BigIntegerField(default = -1)
    rx_errors     = models.BigIntegerField(default = -1)
    tx_packets    = models.BigIntegerField(default = -1)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

class PortDiffStats(models.Model):
    '''Port difference on statistics on the respective port'''
    dpid                = models.BigIntegerField(default = -1)
    tx_dropped          = models.BigIntegerField(default = -1)
    # port_number         = models.BigIntegerField(default = -1)
    rx_packets          = models.BigIntegerField(default = -1)
    rx_crc_err          = models.BigIntegerField(default = -1)
    tx_bytes            = models.BigIntegerField(default = -1)
    rx_dropped          = models.BigIntegerField(default = -1)
    port_no             = models.CharField(default = "No Data Yet", max_length = 50)
    rx_over_err         = models.BigIntegerField(default = -1)
    rx_frame_err        = models.BigIntegerField(default = -1)
    rx_bytes            = models.BigIntegerField(default = -1)
    tx_errors           = models.BigIntegerField(default = -1)
    duration_nsec       = models.BigIntegerField(default = -1)
    collisions          = models.BigIntegerField(default = -1)
    duration_sec        = models.BigIntegerField(default = -1)
    rx_errors           = models.BigIntegerField(default = -1)
    tx_packets          = models.BigIntegerField(default = -1)
    latest_port_fk      = models.ForeignKey(PortStats, on_delete=models.CASCADE, related_name='latest_port', default = 1)
    penultimate_port_fk = models.ForeignKey(PortStats, on_delete=models.CASCADE, related_name='penultimate_port', default = 1)
    time_interval       = models.FloatField(default = -1)
    api_retry           = models.BigIntegerField(default = -1)
    created             = models.DateTimeField(auto_now_add = True)
    last_modified       = models.DateTimeField(auto_now = True)

class FlowAggregateDiffStats(models.Model):
    '''Total amount of packets sent'''
    dpid                = models.BigIntegerField(default = -1)
    packet_count        = models.BigIntegerField(default = -1)
    byte_count          = models.BigIntegerField(default = -1)
    flow_count          = models.BigIntegerField(default = -1)
    latest_flow_fk      = models.ForeignKey(FlowAggregateStats, on_delete=models.CASCADE, related_name='latest_flow', default = 1)
    penultimate_flow_fk = models.ForeignKey(FlowAggregateStats, on_delete=models.CASCADE, related_name='penultimate_flow', default = 1)
    time_interval       = models.FloatField(default = -1)
    api_retry           = models.BigIntegerField(default = -1)
    created             = models.DateTimeField(auto_now_add = True)
    last_modified       = models.DateTimeField(auto_now = True)

class AttackNotification(models.Model):
    '''Attack notification'''
    attack_type   = models.CharField(default = "No Data Yet", max_length = 50) #DDoS, controller comprmise, etc
    attack_vector = models.CharField(default = "No Data Yet", max_length = 50) #Where the attack came from (flow_aggregate, port statistics)
    port_no       = models.CharField(default = "No Data Yet", max_length = 50)
    percentage    = models.FloatField(default = -1) # Percentage of the value from the machine learning model
    threshold     = models.FloatField(default = -1) # Threshold for value to be considered valid
    attack_value  = models.FloatField(default = -1) # Value of the attack
    attack_true   = models.BooleanField(default = 0) # Attack is valid when percentage > threshold
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

class ConfigurationModel(models.Model):
    controllerIP = models.CharField(default = "0.0.0.0", max_length = 50)
    ml_threshold = models.FloatField(default = -1)
    port_threshold = models.BigIntegerField(default = -1)
    port_diff_threshold = models.BigIntegerField(default = -1)
    flow_aggregate_threshold = models.BigIntegerField(default = -1)
    flow_aggregate_difference_threshold = models.BigIntegerField(default = -1)

class Switch(models.Model):
    switch_number = models.BigIntegerField(default=-1)
