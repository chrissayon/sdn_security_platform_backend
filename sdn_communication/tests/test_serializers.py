from django.test import TestCase
from ..serializers import DescStatsSerializer, FlowStatsSerializer, FlowAggregateStatsSerializer, PortStatsSerializer
from ..serializers import FlowAggregateDiffStatsSerializer, PortDiffStatsSerializer
from ..serializers import AttackNotificationSerializer, ConfigurationModelSerializer
from ..models import DescStats, FlowStats, FlowAggregateStats, PortStats
from ..models import FlowAggregateDiffStats, PortDiffStats
from ..models import AttackNotification, ConfigurationModel

class TestSerializers(TestCase):
    def setUp(self):
        DescStats.objects.create(dp_desc='non-existent')
        FlowStats.objects.create(hard_timeout = 50)
        FlowAggregateStats.objects.create(byte_count = 100)
        PortStats.objects.create(tx_dropped = 200)
        FlowAggregateDiffStats.objects.create(byte_count = 1000)
        PortDiffStats.objects.create(tx_dropped = 400)
        AttackNotification.objects.create(percentage = 0.06)
        ConfigurationModel.objects.create(controllerIP = "0.1.2.3")
    
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

    def test_flow_aggregate_diff_stats_serializer(self):
        """Test flow aggregate statics serializer"""
        flow_aggregate_diff_stats = FlowAggregateDiffStats.objects.get(id = 1)
        serializer = FlowAggregateStatsSerializer(flow_aggregate_diff_stats)
        self.assertEqual(serializer.data['byte_count'], 1000)
    
    def test_port_diff_stats_serializer(self):
        """Test port statistics serializer"""
        port_diff_stats = PortDiffStats.objects.get(id = 1)
        serializer = PortStatsSerializer(port_diff_stats)
        self.assertEqual(serializer.data['tx_dropped'], 400)

    def test_attack_notification_serializer(self):
        attack_notification = AttackNotification.objects.get(id = 1)
        serializer = AttackNotificationSerializer(attack_notification)
        self.assertEqual(serializer.data['percentage'], 0.06)

    def test_configuration_serializer(self):
        configuration_model = ConfigurationModel.objects.get(id = 1)
        serializer = ConfigurationModelSerializer(configuration_model)
        self.assertEqual(serializer.data['controllerIP'], "0.1.2.3")