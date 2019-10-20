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
        FlowAggregateStats.objects.create(byte_count = 900)
        PortStats.objects.create(tx_dropped = 200, port_no = 2)
        PortStats.objects.create(tx_dropped = 40, port_no = 3)
        PortStats.objects.create(tx_dropped = 50, port_no = 3)
        PortStats.objects.create(tx_dropped = 300, port_no = 2)
        PortStats.objects.create(tx_dropped = 60, port_no = 3)


    def test_get_desc_stats_view(self):
        '''Testing desciption hardware API'''
        url = reverse('desc_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(json_response['dp_desc'], 'non-existent')

    def test_get_flow_stats_view(self):
        '''Testing get flow stats API'''
        url = reverse('flow_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['hard_timeout'], 50)

    def test_get_flow_aggregate_stats_view(self):
        '''Testing get flow aggregate API'''
        url = reverse('flow_agg_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['byte_count'], 900)

    def test_post_flow_aggregate_stats_view(self):
        '''Testing post flow aggregate stats API'''
        url = reverse('flow_agg_api')
        response = self.client.post(
            url,
            { 'data' : {
                'startDate' : '2018-01-20',
                'endDate'   : '2020-01-20',
                'maxRecords' : 100,
                'startDateYear' : 2018,
                'startDateMonth' : 1,
                'startDateDay' : 20,
                'endDateYear' : 2020,
                'endDateMonth' : 1,
                'endDateDay' : 20,
                }
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_port_stats_view(self):
        '''Testing get port stats API'''
        url = reverse('port_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['tx_dropped'], 60)

    def test_post_port_stats_view(self):
        '''Testing post port stats API'''
        url = reverse('port_api')
        response = self.client.post(
            url,
            { 'data' : {
                'startDate' : '2018-01-20',
                'endDate'   : '2020-01-20',
                'maxRecords' : 100,
                'startDateYear' : 2018,
                'startDateMonth' : 1,
                'startDateDay' : 20,
                'endDateYear' : 2020,
                'endDateMonth' : 1,
                'endDateDay' : 20,
                'port_no' : '3'
                }
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

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


    def test_get_flow_aggregate_diff_stats_view(self):
        '''Testing get view for flow aggregate stats'''
        url = reverse('flow_agg_diff_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        # print(json_response)
        self.assertEqual(json_response[0]['byte_count'], 200)

    def test_post_flow_aggregate_diff_stats_view(self):
        '''Testing post for flow aggregate stats API'''
        url = reverse('flow_agg_diff_api')
        response = self.client.post(
            url,
            { 'data' : {
                'startDate' : '2018-01-20',
                'endDate'   : '2020-01-20',
                'maxRecords' : 100,
                'startDateYear' : 2018,
                'startDateMonth' : 1,
                'startDateDay' : 20,
                'endDateYear' : 2020,
                'endDateMonth' : 1,
                'endDateDay' : 20,
                }
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_port_diff_stats_view(self):
        '''Testing view with for different port stats'''
        url = reverse('port_diff_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        # print(json_response)
        self.assertEqual(json_response[0]['tx_dropped'], 3600)

    def test_post_port_diff_stats_view(self):
        '''Testing flow stats API'''
        url = reverse('flow_agg_diff_api')
        response = self.client.post(
            url,
            { 'data' : {
                'startDate' : '2018-01-20',
                'endDate'   : '2020-01-20',
                'maxRecords' : 100,
                'startDateYear' : 2018,
                'startDateMonth' : 1,
                'startDateDay' : 20,
                'endDateYear' : 2020,
                'endDateMonth' : 1,
                'endDateDay' : 20,
                'port_no' : '3'
                }
            },
            format='json'
        )


        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AttackNotificationView(APITestCase):
    def setUp(self):
        AttackNotification.objects.create(
            percentage=0.3
        )

        AttackNotification.objects.create(
            attack_type   = "Denial of Service",
            attack_vector = "Flow Aggregate",
            percentage    = -2,
            threshold     = 500,
            attack_true   = 1,
        )


    def test_get_attack_notification_view(self):
        '''Testing the machine learnign result'''
        url = reverse('attack_notification_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        # print(json_response)
        self.assertEqual(json_response[0]['percentage'], 0.3)

    def test_post_all_attack_notification_view(self):
        '''Testing post for all filter'''
        url = reverse('attack_notification_api')
        response = self.client.post(
            url,
            { 'data' : {
                'startDate' : '2018-01-20',
                'endDate'   : '2020-01-20',
                'maxRecords' : 100,
                'startDateYear' : 2018,
                'startDateMonth' : 1,
                'startDateDay' : 20,
                'endDateYear' : 2020,
                'endDateMonth' : 1,
                'endDateDay' : 20,
                'filter' : 'All'
                }
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_filter_attack_notification_view(self):
        '''Testing post for filter'''
        url = reverse('attack_notification_api')
        response = self.client.post(
            url,
            { 'data' : {
                'startDate' : '2018-01-20',
                'endDate'   : '2020-01-20',
                'maxRecords' : 100,
                'startDateYear' : 2018,
                'startDateMonth' : 1,
                'startDateDay' : 20,
                'endDateYear' : 2020,
                'endDateMonth' : 1,
                'endDateDay' : 20,
                'filter' : 'Flow Aggregate'
                }
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ConfigurationNoDataView(APITestCase):
    def test_configuration_no_IP(self):
        '''Test writing configuration IP with API'''
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
        '''Test getting configuration IP from database'''
        url = reverse('update_controller_IP_api')
        response = self.client.get(url, format='json')
        # print(response)
        json_response = response.json()
        # print(json_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['controllerIP'], '1.1.1.1')


    def test_write_configuration_IP(self):
        '''Test writing new IP to database'''
        url = reverse('update_controller_IP_api')
        response = self.client.post(
            url,
            { 'data' : {'controllerIP' : "0.0.0.0"} },
            format='json'
        )
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_ml(self):
        '''Test getting machine learning threshold from database'''
        url = reverse('update_ml_api')
        response = self.client.get(url, format='json')
        # print(response)
        json_response = response.json()
        # print(json_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['ml_threshold'], 0.01)

    def test_write_ml(self):
        '''Test writing new machine learning threshold from database'''
        url = reverse('update_ml_api')
        response = self.client.post(
            url,
            { 'data' : {
                'ml_threshold' : 0.01,
                'port_threshold' : 10000000000,
                'port_diff_threshold' : 500,
                'flow_aggregate_threshold' :700000000,
                'flow_aggregate_difference_threshold' :200,
                }},
            format='json'
        )
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GraphViews(APITestCase):
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

    def test_get_port_graph(self):
        url = reverse('port_graph_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_port_diff_graph(self):
        url = reverse('port_diff_graph_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_flow_agg_diff_graph(self):
        url = reverse('flow_agg_diff_graph_api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_port_graph(self):
        url = reverse('port_graph_api')
        response = self.client.post(
            url,
            { 'data' : {
                'maxRecords' : 100,
                }
            },
            format='json'
        )
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_port_diff_graph(self):
        url = reverse('port_diff_graph_api')
        response = self.client.post(
            url,
            { 'data' : {
                'maxRecords' : 100,
                }
            },
            format='json'
        )
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_flow_agg_diff_graph(self):
        url = reverse('flow_agg_diff_graph_api')
        response = self.client.post(
            url,
            { 'data' : {
                'maxRecords' : 100,
                }
            },
            format='json'
        )
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
