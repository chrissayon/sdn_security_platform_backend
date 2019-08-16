from django.db import models


class DescStats(models.Model):
    '''Model for hardware description'''
    dp_desc       = models.CharField(default = "", max_length = 50)
    mfr_desc      = models.CharField(default = "", max_length = 50)
    hw_desc       = models.CharField(default = "", max_length = 50)
    sw_desc       = models.CharField(default = "", max_length = 50)
    serial_num    = models.CharField(default = "", max_length = 50)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class FlowStats(models.Model):
    '''Flow Table information'''
    dpid          = models.IntegerField(default = 0)
    actions       = models.CharField(default = "", max_length = 50)
    idle_timeout  = models.IntegerField(default = 0)
    cookie        = models.IntegerField(default = 0)
    packet_count  = models.IntegerField(default = 0)
    hard_timeout  = models.IntegerField(default = 0)
    byte_count    = models.IntegerField(default = 0)
    duration_sec  = models.IntegerField(default = 0)
    duration_nsec = models.IntegerField(default = 0)
    priority      = models.IntegerField(default = 0)
    length        = models.IntegerField(default = 0)
    flags         = models.IntegerField(default = 0)
    table_id      = models.IntegerField(default = 0)
    match         = models.CharField(default = "", max_length = 50)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    

class FlowAggregateStats(models.Model):
    '''Total amount of packets sent'''
    dpid          = models.IntegerField(default = 0)
    packet_count  = models.IntegerField(default = 0)
    byte_count    = models.IntegerField(default = 0)
    flow_count    = models.IntegerField(default = 0)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class TableStats(models.Model):
    '''Need to resolve the redundant tables that go over 100+'''
    dpid          = models.IntegerField(default = 0)
    table_id      = models.IntegerField(default = 0)
    matched_count = models.IntegerField(default = 0)
    lookup_count  = models.IntegerField(default = 0)
    active_count  = models.IntegerField(default = 0)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class PortStats(models.Model):
    '''Statistics on the respective port'''
    dpid          = models.IntegerField(default = 0)
    tx_dropped    = models.IntegerField(default = 0)
    port_number   = models.IntegerField(default = 0)
    rx_packets    = models.IntegerField(default = 0)
    rx_crc_err    = models.IntegerField(default = 0)
    tx_bytes      = models.IntegerField(default = 0)
    rx_dropped    = models.IntegerField(default = 0)
    port_no       = models.CharField(default = "", max_length = 50)
    rx_over_err   = models.IntegerField(default = 0)
    rx_frame_err  = models.IntegerField(default = 0)
    rx_bytes      = models.IntegerField(default = 0)
    tx_errors     = models.IntegerField(default = 0)
    duration_nsec = models.IntegerField(default = 0)
    collisions    = models.IntegerField(default = 0)
    duration_sec  = models.IntegerField(default = 0)
    rx_errors     = models.IntegerField(default = 0)
    tx_packets    = models.IntegerField(default = 0)
    created       = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


class Switch(models.Model):
    switch_number = models.IntegerField(default=0)
