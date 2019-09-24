from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import DescStats, FlowStats, FlowAggregateStats, PortStats
from ..models import FlowAggregateDiffStats, PortDiffStats
from ..models import AttackNotification, ConfigurationModel
from sdn_communication.tasks import write_flow_agg_diff_stats, write_port_diff_stats
from django.urls import reverse

class TestViews(APITestCase):
    def setUp(self):
        DescStats.objects.create(dp_desc="non-existent")
        FlowStats.objects.create(hard_timeout = 50)
        FlowAggregateStats.objects.create(byte_count = 100)
        PortStats.objects.create(tx_dropped = 200, port_no = 2)
        PortStats.objects.create(tx_dropped = 40, port_no = 3)
        PortStats.objects.create(tx_dropped = 50, port_no = 3)
        PortStats.objects.create(tx_dropped = 300, port_no = 2)
        PortStats.objects.create(tx_dropped = 60, port_no = 3)


    def test_desc_stats_view(self):
        '''Testing desciption hardware API'''
        url = reverse('desc_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(json_response['dp_desc'], 'non-existent')
    
    def test_flow_stats_view(self):
        '''Testing flow stats API'''
        url = reverse('flow_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['hard_timeout'], 50)

    def test_flow_aggregate_stats_view(self):
        '''Testing flow aggregate API'''
        url = reverse('flow_agg_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['byte_count'], 100)

    def test_port_stats_view(self):
        '''Testing port stats API'''
        url = reverse('port_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['tx_dropped'], 60)
    
    # def test_flow_aggregate_diff_view(self):
    #     url = reverse('flow_agg_diff_api')
    #     response = self.client.get(url, format='json')
    #     json_response = response.json()
    #     self.assertEqual(1, 1)

    # def test_port_diff_view(self):
    #     url = reverse('port_diff_api')
    #     response = self.client.get(url, format='json')
    #     json_response = response.json()
    #     self.assertEqual(json_response['tx_dropped'], 10)

class TestDiffViews(APITestCase):
    def setUp(self):
        PortStats.objects.create(tx_dropped = 200, port_no = 2)
        PortStats.objects.create(tx_dropped = 400, port_no = 2)
        write_port_diff_stats(2)
        PortStats.objects.create(tx_dropped = 500, port_no = 2)
        PortStats.objects.create(tx_dropped = 4100, port_no = 2)
        write_port_diff_stats(2)
        PortStats.objects.create(tx_dropped = 5100, port_no = 2)
        PortStats.objects.create(tx_dropped = 6100, port_no = 2)
        write_port_diff_stats(2)
        PortStats.objects.create(tx_dropped = 7000, port_no = 2)
        PortStats.objects.create(tx_dropped = 7000, port_no = 2)
        write_port_diff_stats(2)
        PortStats.objects.create(tx_dropped = 8000, port_no = 2)
        PortStats.objects.create(tx_dropped = 8500, port_no = 2)
        write_port_diff_stats(2)
        
        PortStats.objects.create(tx_dropped = 200, port_no = 3)
        PortStats.objects.create(tx_dropped = 400, port_no = 3)
        write_port_diff_stats(3)
        PortStats.objects.create(tx_dropped = 500, port_no = 3)
        write_port_diff_stats(3)
        PortStats.objects.create(tx_dropped = 4100, port_no = 3)
        write_port_diff_stats(3)
        PortStats.objects.create(tx_dropped = 5100, port_no = 3)
        write_port_diff_stats(3)
        PortStats.objects.create(tx_dropped = 6100, port_no = 3)
        write_port_diff_stats(3)
        PortStats.objects.create(tx_dropped = 7000, port_no = 3)
        write_port_diff_stats(3)
        PortStats.objects.create(tx_dropped = 7000, port_no = 3)
        write_port_diff_stats(3)
        PortStats.objects.create(tx_dropped = 8000, port_no = 3)
        write_port_diff_stats(3)
        PortStats.objects.create(tx_dropped = 8500, port_no = 3)
        write_port_diff_stats(3)

        FlowAggregateStats.objects.create(byte_count = 1)
        FlowAggregateStats.objects.create(byte_count = 5)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 10)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 100)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 300)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 500)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 800)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 1000)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 10010)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 20000)
        write_flow_agg_diff_stats()
        FlowAggregateStats.objects.create(byte_count = 30000)
        write_flow_agg_diff_stats()


    def test_flow_aggregate_diff_stats_view(self):
        '''Testing view for different flow aggregate stats'''
        url = reverse('flow_agg_diff_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        # print(json_response)
        self.assertEqual(json_response[0]['byte_count'], 200)
    
    def test_port_diff_stats_view(self):
        '''Testing view with for different port stats'''
        url = reverse('port_diff_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        # print(json_response)
        self.assertEqual(json_response[0]['tx_dropped'], 3600)

class AttackNotificationView(APITestCase):
    def setUp(self):
        AttackNotification.objects.create(percentage=0.3)

    def test_attack_notification_view(self):
        '''Testing the machine learnign result'''
        url = reverse('attack_notification_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        # print(json_response)
        self.assertEqual(json_response[0]['percentage'], 0.3)

class ConfigurationNoDataView(APITestCase):
    def test_configuration_no_IP(self):
        url = reverse('update_controller_IP_api')
        response = self.client.post(
            url, 
            { 'data' : {'controllerIP' : "0.0.0.0"} }, 
            format='json'
        )
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ConfigurationDataView(APITestCase):
    def setUp(self):
        configuration_instance = ConfigurationModel.objects.create(
            controllerIP = "1.1.1.1",
            ml_threshold = 0.01
        )
    
    def test_get_configuration_IP(self):
        url = reverse('update_controller_IP_api')
        response = self.client.get(url, format='json')
        # print(response)
        json_response = response.json()
        # print(json_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['controllerIP'], '1.1.1.1')


    def test_write_configuration_IP(self):
        url = reverse('update_controller_IP_api')
        response = self.client.post(
            url, 
            { 'data' : {'controllerIP' : "0.0.0.0"} }, 
            format='json'
        )
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_ml(self):
        url = reverse('update_ml_api')
        response = self.client.get(url, format='json')
        # print(response)
        json_response = response.json()
        # print(json_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['ml_threshold'], 0.01)

    def test_write_ml(self):
        url = reverse('update_ml_api')
        response = self.client.post(
            url, 
            { 'data' : {'ml_threshold' : 0.01} }, 
            format='json'
        )
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    