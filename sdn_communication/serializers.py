from rest_framework import serializers
from .models import DescStats, FlowStats, FlowAggregateStats, PortStats
from .models import FlowAggregateDiffStats, PortDiffStats
from .models import AttackNotification, ConfigurationModel

class DescStatsSerializer(serializers.ModelSerializer):
    '''Serializer for hardware description'''
    class Meta:
        model = DescStats
        fields = '__all__'
    
class FlowStatsSerializer(serializers.ModelSerializer):
    '''Serializer for flow statistcs'''
    class Meta:
        model = FlowStats
        fields = '__all__'

class FlowAggregateStatsSerializer(serializers.ModelSerializer):
    '''Serializer for flow statistcs'''
    class Meta:
        model = FlowAggregateStats
        fields = '__all__'

class PortStatsSerializer(serializers.ModelSerializer):
    '''Serializer for flow statistcs'''
    class Meta:
        model = PortStats
        fields = '__all__'

class FlowAggregateDiffStatsSerializer(serializers.ModelSerializer):
    '''Serializer for flow statistcs'''
    class Meta:
        model = FlowAggregateDiffStats
        fields = '__all__'

class PortDiffStatsSerializer(serializers.ModelSerializer):
    '''Serializer for flow statistcs'''
    class Meta:
        model = PortDiffStats
        fields = '__all__'

class AttackNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttackNotification
        fields = '__all__'

class ConfigurationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationModel
        fields = '__all__'