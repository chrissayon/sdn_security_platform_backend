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
    dpid          = models.IntegerField(default = -1)
    actions       = models.CharField(default = "No Data Yet", max_length = 50)
    idle_timeout  = models.IntegerField(default = -1)
    cookie        = models.IntegerField(default = -1)
    packet_count  = models.IntegerField(default = -1)
    hard_timeout  = models.IntegerField(default = -1)
    byte_count    = models.IntegerField(default = -1)
    duration_sec  = models.IntegerField(default = -1)
    duration_nsec = models.IntegerField(default = -1)
    priority      = models.IntegerField(default = -1)
    length        = models.IntegerField(default = -1)
    flags         = models.IntegerField(default = -1)
    table_id      = models.IntegerField(default = -1)
    match         = models.CharField(default = "No Data Yet", max_length = 50)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class FlowAggregateStats(models.Model):
    '''Total amount of packets sent'''
    dpid          = models.IntegerField(default = -1)
    packet_count  = models.IntegerField(default = -1)
    byte_count    = models.IntegerField(default = -1)
    flow_count    = models.IntegerField(default = -1)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class TableStats(models.Model):
    '''Need to resolve the redundant tables that go over 100+'''
    dpid          = models.IntegerField(default = -1)
    table_id      = models.IntegerField(default = -1)
    matched_count = models.IntegerField(default = -1)
    lookup_count  = models.IntegerField(default = -1)
    active_count  = models.IntegerField(default = -1)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class PortStats(models.Model):
    '''Statistics on the respective port'''
    dpid          = models.IntegerField(default = -1)
    tx_dropped    = models.IntegerField(default = -1)
    # port_number   = models.IntegerField(default = -1)
    rx_packets    = models.IntegerField(default = -1)
    rx_crc_err    = models.IntegerField(default = -1)
    tx_bytes      = models.IntegerField(default = -1)
    rx_dropped    = models.IntegerField(default = -1)
    port_no       = models.CharField(default = "No Data Yet", max_length = 50)
    rx_over_err   = models.IntegerField(default = -1)
    rx_frame_err  = models.IntegerField(default = -1)
    rx_bytes      = models.IntegerField(default = -1)
    tx_errors     = models.IntegerField(default = -1)
    duration_nsec = models.IntegerField(default = -1)
    collisions    = models.IntegerField(default = -1)
    duration_sec  = models.IntegerField(default = -1)
    rx_errors     = models.IntegerField(default = -1)
    tx_packets    = models.IntegerField(default = -1)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

class PortDiffStats(models.Model):
    '''Port difference on statistics on the respective port'''
    dpid                = models.IntegerField(default = -1)
    tx_dropped          = models.IntegerField(default = -1)
    # port_number         = models.IntegerField(default = -1)
    rx_packets          = models.IntegerField(default = -1)
    rx_crc_err          = models.IntegerField(default = -1)
    tx_bytes            = models.IntegerField(default = -1)
    rx_dropped          = models.IntegerField(default = -1)
    port_no             = models.CharField(default = "No Data Yet", max_length = 50)
    rx_over_err         = models.IntegerField(default = -1)
    rx_frame_err        = models.IntegerField(default = -1)
    rx_bytes            = models.IntegerField(default = -1)
    tx_errors           = models.IntegerField(default = -1)
    duration_nsec       = models.IntegerField(default = -1)
    collisions          = models.IntegerField(default = -1)
    duration_sec        = models.IntegerField(default = -1)
    rx_errors           = models.IntegerField(default = -1)
    tx_packets          = models.IntegerField(default = -1)
    latest_port_fk      = models.ForeignKey(PortStats, on_delete=models.CASCADE, related_name='latest_port', default = 1)
    penultimate_port_fk = models.ForeignKey(PortStats, on_delete=models.CASCADE, related_name='penultimate_port', default = 1)
    time_interval       = models.FloatField(default = -1)
    api_retry           = models.IntegerField(default = -1)
    created             = models.DateTimeField(auto_now_add = True)
    last_modified       = models.DateTimeField(auto_now = True)

class FlowAggregateDiffStats(models.Model):
    '''Total amount of packets sent'''
    dpid                = models.IntegerField(default = -1)
    packet_count        = models.IntegerField(default = -1)
    byte_count          = models.IntegerField(default = -1)
    flow_count          = models.IntegerField(default = -1)
    latest_flow_fk      = models.ForeignKey(FlowAggregateStats, on_delete=models.CASCADE, related_name='latest_flow', default = 1)
    penultimate_flow_fk = models.ForeignKey(FlowAggregateStats, on_delete=models.CASCADE, related_name='penultimate_flow', default = 1)
    time_interval       = models.FloatField(default = -1)
    api_retry           = models.IntegerField(default = -1)
    created             = models.DateTimeField(auto_now_add = True)
    last_modified       = models.DateTimeField(auto_now = True)

class AttackNotification(models.Model):
    '''Attack notification'''
    attack_type   = models.CharField(default = "No Data Yet", max_length = 50) #DDoS, controller comprmise, etc
    attack_vector = models.CharField(default = "No Data Yet", max_length = 50) #Where the attack came from (flow_aggregate, port statistics)
    percentage    = models.FloatField(default = -1) # Percentage of the value from the machine learning model
    threshold     = models.FloatField(default = -1) # Threshold for value to be considered valid
    attack_true   = models.BooleanField(default = 0) # Attack is valid when percentage > threshold
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

class Switch(models.Model):
    switch_number = models.IntegerField(default=-1)
