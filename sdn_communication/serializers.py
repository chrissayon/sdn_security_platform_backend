from rest_framework import serializers
from .models import DescStats

class DescStatsSerializer(serializers.ModelSerializer):
    '''Model for hardware description'''
    class Meta:
        model = DescStats
        fields = '__all__'