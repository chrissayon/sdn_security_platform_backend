from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import DescStats, FlowStats, FlowAggregateStats, PortStats
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
        self.assertEqual(json_response[0]['tx_dropped'], 200)
    
    def test_flow_aggregate_diff_view(self):
        url = reverse('flow_agg_diff_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(1, 1)

    def test_port_diff_view(self):
        url = reverse('port_diff_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(json_response['tx_dropped'], 10)