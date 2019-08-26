from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DescStats, FlowStats, FlowAggregateStats, PortStats
from .models import FlowAggregateDiffStats, PortDiffStats
from .serializers import DescStatsSerializer, FlowStatsSerializer,FlowAggregateStatsSerializer, PortStatsSerializer
from .serializers import FlowAggregateDiffStatsSerializer, PortDiffStatsSerializer

# List switch hardware description
class DescStatsView(APIView):

    def get(self, request):
        '''Obtain Switcch description from database'''
        desc_stats = DescStats.objects.get(id=1)
        serializer = DescStatsSerializer(desc_stats)
        #print(serializer.data)
        return Response(serializer.data)

class FlowStatsView(APIView):

    def get(self, request):
        '''Obtain flow statistics from database'''
        flow_stats = FlowStats.objects.all()
        serializer = FlowStatsSerializer(flow_stats, many=True)
        #print(serializer.data)
        return Response(serializer.data)

class FlowAggregateStatsView(APIView):

    def get(self, request):
        '''Obtain flow aggregate statistics from database'''
        flow_agg_stats = FlowAggregateStats.objects.get(id = 1)
        serializer = FlowStatsSerializer(flow_agg_stats)
        #print(serializer.data)
        return Response(serializer.data)

class PortStatsView(APIView):

    def get(self, request):
        '''Obtain all port statistics from database'''
        port_stats = PortStats.objects.order_by('-id')[:100]
        port_stats_reversed = reversed(port_stats)
        serializer = PortStatsSerializer(port_stats, many=True)
        #print(serializer.data)
        return Response(serializer.data)

class FlowAggregateDiffStatsView(APIView):

    def get(self, request):
        '''Get the flow aggregate statistics difference'''
        flow_agg_diff_stats = FlowAggregateDiffStats.objects.order_by('-id')[:7]
        flow_agg_diff_stats_reversed = reversed(flow_agg_diff_stats)
        serializer = FlowAggregateDiffStatsSerializer(flow_agg_diff_stats_reversed, many=True)
        return Response(serializer.data)


class PortDiffStatsView(APIView):

    def get(self, request):
        '''Get the port statistics difference'''
        #latest_port_stats = PortStats.objects.order_by('id').reverse()[1]
        port_diff_stats = PortDiffStats.objects.filter(port_no = 3).order_by('-id')[:7]
        port_diff_stats_reversed = reversed(port_diff_stats)
        serializer = PortDiffStatsSerializer(port_diff_stats_reversed, many=True)
        return Response(serializer.data)