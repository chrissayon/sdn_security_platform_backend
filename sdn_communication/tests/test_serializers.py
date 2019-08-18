from django.test import TestCase
from ..serializers import DescStatsSerializer, FlowStatsSerializer,FlowAggregateStatsSerializer, PortStatsSerializer
from ..models import DescStats, FlowStats, FlowAggregateStats, PortStats

class TestSerializers(TestCase):
    def setUp(self):
        DescStats.objects.create(dp_desc='non-existent')
        FlowStats.objects.create(hard_timeout = 50)
        FlowAggregateStats.objects.create(byte_count = 100)
        PortStats.objects.create(tx_dropped = 200)
    
    def test_desk_stats_serializer(self):
        """Test desciption serializer"""
        desc_stats = DescStats.objects.get(id = 1)
        serializer = DescStatsSerializer(desc_stats)
        self.assertEqual(serializer.data['dp_desc'], 'non-existent')
    
    def test_flow_stats_serializer(self):
        """Test flow statistics serializer"""
        flow_stats = FlowStats.objects.get(id = 1)
        serializer = FlowStatsSerializer(flow_stats)
        self.assertEqual(serializer.data['hard_timeout'], 50)
        
    def test_flow_aggregate_stats_serializer(self):
        """Test flow aggregate statics serializer"""
        flow_aggregate_stats = FlowAggregateStats.objects.get(id = 1)
        serializer = FlowAggregateStatsSerializer(flow_aggregate_stats)
        self.assertEqual(serializer.data['byte_count'], 100)
        
    def test_port_stats_serializer(self):
        """Test port statistics serializer"""
        port_stats = PortStats.objects.get(id = 1)
        serializer = PortStatsSerializer(port_stats)
        self.assertEqual(serializer.data['tx_dropped'], 200)