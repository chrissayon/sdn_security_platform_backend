from rest_framework import serializers
from .models import DescStats, FlowStats, FlowAggregateStats, PortStats

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


