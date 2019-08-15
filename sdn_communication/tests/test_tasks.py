from django.test import TestCase
from sdn_communication.tasks import get_switch_number, get_switch_desc, get_flow_stats, get_agg_flow_stats, get_port_stats
from sdn_communication.tasks import write_switch_desc
from sdn_communication.models import Switch, DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats 
from rest_framework import status
from requests.models import Response

class TasksTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.switch_desc_response = Response()
        cls.switch_desc_response.status_code = 200
        cls.switch_desc_response._content = b'{ "1" : {"dp_desc" : "Apple",\
            "mfr_desc" : "Banana", \
            "hw_desc" : "Carrot", \
            "sw_desc" : "Durian", \
            "serial_num" : "1234" }}'


    def test_write_switch_desc(self):
        """Writing the hardware description"""
        #switch_desc = DescStats.objects.get(dp_desc = "Apple")
        self.assertEqual(write_switch_desc(self.switch_desc_response), True)