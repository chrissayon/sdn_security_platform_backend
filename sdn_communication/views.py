from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DescStats, FlowStats, FlowAggregateStats, PortStats
from .serializers import DescStatsSerializer, FlowStatsSerializer,FlowAggregateStatsSerializer, PortStatsSerializer

# List switch hardware description
class DescStatsView(APIView):

    def get(self, request):
        desc_stats = DescStats.objects.get(id=1)
        serializer = DescStatsSerializer(desc_stats)
        #print(serializer.data)
        return Response(serializer.data)

class FlowStatsView(APIView):

    def get(self, request):
        flow_stats = FlowStats.objects.all()
        serializer = FlowStatsSerializer(flow_stats, many=True)
        #print(serializer.data)
        return Response(serializer.data)

class FlowAggregateStatsView(APIView):

    def get(self, request):
        flow_agg_stats = FlowAggregateStats.objects.get(id = 1)
        serializer = FlowStatsSerializer(flow_agg_stats)
        #print(serializer.data)
        return Response(serializer.data)

class PortStatsView(APIView):

    def get(self, request):
        port_stats = PortStats.objects.all()
        serializer = PortStatsSerializer(port_stats, many=True)
        #print(serializer.data)
        return Response(serializer.data)
