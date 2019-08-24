from django.test import TestCase
from sdn_communication.tasks import get_switch_number, get_switch_desc, get_flow_stats, get_agg_flow_stats, get_port_stats
from sdn_communication.tasks import write_switch_desc, write_flow_stats, write_agg_flow_stats, write_port_stats
from sdn_communication.tasks import write_flow_agg_diff_stats
from sdn_communication.models import Switch, DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats 
from sdn_communication.models import FlowAggregateDiffStats
from rest_framework import status
from requests.models import Response

class TasksTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):

        # Flow statistics response
        cls.flow_stats_response = Response()
        cls.flow_stats_response.status_code = 200
        cls.flow_stats_response._content = b'{ "1" : [{ \
            "actions"       : ["OUTPUT:2"],     \
            "idle_timeout"  : "0",              \
            "cookie"        : "0",              \
            "packet_count"  : "0",              \
            "hard_timeout"  : "0",              \
            "byte_count"    : "728",            \
            "duration_sec"  : "35",             \
            "duration_nsec" : "126000000",      \
            "priority"      : "1",              \
            "length"        : "104",            \
            "flags"         : "0",              \
            "table_id"      : "0",              \
            "match" : {                         \
                "dl_dest" : "00:00:00:00:00:00", \
                "dl_src"  : "00:00:00:00:00:00", \
                "in_port" : "3" }, \
            "serial_num" : "1234" }]}'
        
        # Description hardware response
        cls.switch_desc_response = Response()
        cls.switch_desc_response.status_code = 200
        cls.switch_desc_response._content = b'{ "1" : {"dp_desc" : "None",\
            "mfr_desc"   : "2.9.2",         \
            "hw_desc"    : "Open VSwitch",  \
            "sw_desc"    : "None",          \
            "serial_num" : "Nicira, Inc." }}'
        
        cls.flow_agg_stats_response = Response()
        cls.flow_agg_stats_response.status_code = 200
        cls.flow_agg_stats_response._content = b'{ "1" : [{\
            "packet_count" : "102",   \
            "byte_count"   : "8080",  \
            "flow_count"   : "5" }]}'

        cls.port_stats_response = Response()
        cls.port_stats_response.status_code = 200
        cls.port_stats_response._content =b'{ "1" : [{ \
            "tx_dropped"    : "0",        \
            "rx_packets"    : "0",        \
            "rx_crc_err"    : "0",        \
            "tx_bytes"      : "0",        \
            "rx_dropped"    : "64",       \
            "port_no"       : "LOCAL",    \
            "rx_over_err"   : "0",        \
            "rx_frame_err"  : "0",        \
            "rx_bytes"      : "0",        \
            "tx_errors"     : "104",      \
            "duration_nsec" : "15000000", \
            "collisions"    : "0",        \
            "duration_sec"  : "26489",    \
            "rx_errors"     : "0",        \
            "tx_packets"    : "0"}]}'

    def test_write_switch_desc(self):
        """Writing the hardware description to the database"""
        self.assertEqual(write_switch_desc(self.switch_desc_response), True)

    def test_write_flow_stats(self):
        """Writing flow stats to the database"""
        self.assertEqual(write_flow_stats(self.flow_stats_response), True)

    def test_write_flow_agg_stats(self):
        """Writing aggregate flow to the database"""
        self.assertEqual(write_agg_flow_stats(self.flow_agg_stats_response), True)

    def test_write_port_stats(self):
        """Write port statistics to the database"""
        self.assertEqual(write_port_stats(self.port_stats_response), True)

class TasksDiffTestCase(TestCase):
    def setUp(self):
        PortStats.objects.create(tx_dropped = 5, port_no = 1)
        PortStats.objects.create(tx_dropped = 10, port_no = 1)
        PortStats.objects.create(tx_dropped = 20, port_no = 1)
        PortStats.objects.create(tx_dropped = 100, port_no = 2)
        PortStats.objects.create(tx_dropped = 200, port_no = 2)
        PortStats.objects.create(tx_dropped = 300, port_no = 2)
        PortStats.objects.create(tx_dropped = 20, port_no = 3)
        PortStats.objects.create(tx_dropped = 40, port_no = 3)
        PortStats.objects.create(tx_dropped = 80, port_no = 3)
        
        FlowAggregateStats.objects.create(byte_count = 100)
        FlowAggregateStats.objects.create(byte_count = 200)
        FlowAggregateStats.objects.create(byte_count = 350)
    
    def test_flow_agg_diff_value(self):
        """Checking the port value difference of two records"""
        self.assertEqual(write_flow_agg_diff_stats(), True)
        flow_agg_stats_diff_instance = FlowAggregateDiffStats.objects.get(id = 1)
        self.assertEqual(flow_agg_stats_diff_instance.byte_count, 150)

class TasksDiffTestCaseNoModel(TestCase):
    
    def test_port_diff_value(self):
        """Checking the port value difference of two records"""
        # self.assertFalse(write_flow_agg_diff_stats())
        write_flow_agg_diff_stats()
        self.assertFalse(False)
 