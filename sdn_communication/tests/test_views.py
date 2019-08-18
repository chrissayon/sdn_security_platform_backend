from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import DescStats, FlowStats, FlowAggregateStats
from ..views import DescStatsView
from django.urls import reverse

class test(APITestCase):
    def setUp(self):
        DescStats.objects.create(dp_desc="non-existent")

    def test_desc_stats_view(self):
        '''Testing desciption hardware view'''
        url = reverse('desc-api')
        response = self.client.get(url, format='json')
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]['dp_desc'], 'non-existent')