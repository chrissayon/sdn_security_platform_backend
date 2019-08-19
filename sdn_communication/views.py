from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DescStats, FlowStats, FlowAggregateStats, PortStats
from .serializers import DescStatsSerializer, FlowStatsSerializer,FlowAggregateStatsSerializer, PortStatsSerializer

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
        port_stats = PortStats.objects.all()
        serializer = PortStatsSerializer(port_stats, many=True)
        #print(serializer.data)
        return Response(serializer.data)

class FlowAggregateDiffView(APIView):

    def get(self, request):
        '''Get the flow aggregate statistics difference'''
        latest_flow_agg_stats = FlowAggregateStats.objects.order_by('-id')[0]
        serializer = FlowStatsSerializer(latest_flow_agg_stats)
        return Response(serializer.data)

class PortDiffView(APIView):

    def get(self, request):
        '''Get the port statistics difference'''
        #latest_port_stats = PortStats.objects.order_by('id').reverse()[1]
        port_stats = PortStats.objects.filter(port_no = 3)
        length_port = len(port_stats)

        latest_port_stats = port_stats[length_port - 1]
        penultimate_port_stats = port_stats[length_port - 2]

        latest_port_stats.tx_dropped    -= penultimate_port_stats.tx_dropped
        latest_port_stats.rx_packets    -= penultimate_port_stats.rx_packets
        latest_port_stats.rx_crc_err    -= penultimate_port_stats.rx_crc_err
        latest_port_stats.tx_bytes      -= penultimate_port_stats.tx_bytes
        latest_port_stats.rx_dropped    -= penultimate_port_stats.rx_dropped
        latest_port_stats.rx_over_err   -= penultimate_port_stats.rx_over_err
        latest_port_stats.rx_frame_err  -= penultimate_port_stats.rx_frame_err
        latest_port_stats.rx_bytes      -= penultimate_port_stats.rx_bytes
        latest_port_stats.tx_errors     -= penultimate_port_stats.tx_errors
        latest_port_stats.duration_nsec -= penultimate_port_stats.duration_nsec
        latest_port_stats.collisions    -= penultimate_port_stats.collisions
        latest_port_stats.duration_sec  -= penultimate_port_stats.duration_sec
        latest_port_stats.rx_errors     -= penultimate_port_stats.rx_errors
        latest_port_stats.tx_packets    -= penultimate_port_stats.tx_packets

        serializer = PortStatsSerializer(latest_port_stats)

        return Response(serializer.data)