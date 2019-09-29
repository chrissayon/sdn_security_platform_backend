from django.test import TestCase
from sdn_communication.tasks import get_switch_number, get_switch_desc, get_flow_stats, get_agg_flow_stats, get_port_stats
from sdn_communication.tasks import write_switch_desc, write_flow_stats, write_agg_flow_stats, write_port_stats
from sdn_communication.tasks import write_flow_agg_diff_stats, write_port_diff_stats
from sdn_communication.tasks import ml_flow_agg_diff_stats, flow_aggregate_difference_threshold
from sdn_communication.tasks import flow_aggregate_threshold, port_threshold, port_diff_threshold
from sdn_communication.models import Switch, DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats 
from sdn_communication.models import FlowAggregateDiffStats, PortDiffStats, ConfigurationModel
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
    
    def test_flow_agg_diff(self):
        """Writing the flow aggregate difference of two records"""
        self.assertEqual(write_flow_agg_diff_stats(), True)
        flow_agg_stats_diff_instance = FlowAggregateDiffStats.objects.get(id = 1)
        # print(flow_agg_stats_diff_instance.penultimate_flow_fk.id)
        self.assertEqual(flow_agg_stats_diff_instance.byte_count, 150)

    def test_port_diff(self):
        """Writing the port value difference of two records"""
        self.assertEqual(write_port_diff_stats(1), True)
        port_stats_diff_instance = PortDiffStats.objects.get(id = 1)
        # print(flow_agg_stats_diff_instance.penultimate_flow_fk.id)
        self.assertEqual(port_stats_diff_instance.tx_dropped, 10)

class TasksDiffTestCaseNoModel(TestCase):
    
    def test_flow_agg_diff_no_model(self):
        """Checking the port value difference of two records"""
        self.assertFalse(write_flow_agg_diff_stats())
        write_flow_agg_diff_stats()
        self.assertFalse(False)
 
class TasksMachineLearning(TestCase):
    def setUp(self):
        FlowAggregateDiffStats.objects.create(
            packet_count = 0,
            byte_count = 0,
            flow_count = 3,
            latest_flow_fk = FlowAggregateStats.objects.create(),
            penultimate_flow_fk = FlowAggregateStats.objects.create()
            # time = 10,
            # api_retry = 0
        )


    def test_machine_learning_agg_stats(self):
        '''Test machine learning'''
        self.assertTrue(ml_flow_agg_diff_stats(0.1))

class TasksThresholdsPass(TestCase):
    def setUp(self):
        ConfigurationModel.objects.create(
            ml_threshold = 0.01, 
            port_threshold = 500,
            port_diff_threshold = 500,
            flow_aggregate_threshold = 500,
            flow_aggregate_difference_threshold = 500,
        )

        FlowAggregateStats.objects.create(
            byte_count = 1000
        )

        FlowAggregateDiffStats.objects.create(
            packet_count = 1000,
            byte_count = 1000,
            flow_count = 1000,
            latest_flow_fk = FlowAggregateStats.objects.create(byte_count = 1000),
            penultimate_flow_fk = FlowAggregateStats.objects.create(byte_count = 1000)
            # time = 10,
            # api_retry = 0
        )

        PortStats.objects.create(
            port_no = '1',
            rx_bytes = 1000,
        )

        PortDiffStats.objects.create(
            port_no = '1',
            rx_bytes = 1000,
        )

    def test_flow_aggregate_threshold_pass(self):
        '''Test Flow Aggregate Threshold'''
        result = flow_aggregate_threshold()
        self.assertTrue(result)

    def test_flow_aggregate_difference_threshold_pass(self):
        '''Test Flow Aggregate Difference Threshold'''
        result = flow_aggregate_difference_threshold()
        self.assertTrue(result)
    
    def test_port_threshold_pass(self):
        '''Test Port Threshold'''
        result = port_threshold('1')
        self.assertTrue(result)

    def test_port_difference_threshold_pass(self):
        '''Test Port Difference Threshold'''
        result = port_diff_threshold('1')
        self.assertTrue(result)

class TasksThresholdsFail(TestCase):
    def setUp(self):
        FlowAggregateDiffStats.objects.create(
            packet_count = 0,
            byte_count = 500,
            flow_count = 0,
            latest_flow_fk = FlowAggregateStats.objects.create(),
            penultimate_flow_fk = FlowAggregateStats.objects.create()
            # time = 10,
            # api_retry = 0
        )

        ConfigurationModel.objects.create(
            ml_threshold = 0.01, 
            port_threshold = 1000,
            port_diff_threshold = 1000,
            flow_aggregate_threshold = 1000,
            flow_aggregate_difference_threshold = 1000,
        )
    
        FlowAggregateStats.objects.create(byte_count = 0)


        PortStats.objects.create(
            port_no = '1',
            rx_bytes = 500,
        )

        PortDiffStats.objects.create(
            port_no = '1',
            rx_bytes = 500,
        )

    def test_flow_aggregate_threshold_fail(self):
        '''Test Flow Aggregate Threshold'''
        result = flow_aggregate_threshold()
        self.assertFalse(result)

    def test_flow_aggregate_difference_threshold_fail(self):
        '''Test Flow Aggregate Difference Threshold'''
        result = flow_aggregate_difference_threshold()
        self.assertFalse(result)
    
    def test_port_threshold_fail(self):
        '''Test Port Threshold'''
        result = port_threshold('1')
        self.assertFalse(result)

    def test_port_difference_threshold_fail(self):
        '''Test Port Difference Threshold'''
        result = port_diff_threshold('1')
        self.assertFalse(result)
