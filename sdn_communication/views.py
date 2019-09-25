from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DescStats, FlowStats, FlowAggregateStats, PortStats
from .models import FlowAggregateDiffStats, PortDiffStats
from .models import AttackNotification, ConfigurationModel
from .serializers import DescStatsSerializer, FlowStatsSerializer,FlowAggregateStatsSerializer, PortStatsSerializer
from .serializers import FlowAggregateDiffStatsSerializer, PortDiffStatsSerializer
from .serializers import AttackNotificationSerializer, ConfigurationModelSerializer

import json 
from datetime import date

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

    def post(self, request):
        '''Obtain flow aggregate statistics from database'''
        data = json.loads(request.body.decode('utf-8'))
        # print(data)
        maxRecords = data['data']['maxRecords']
        startDateYear = data['data']['startDateYear'] 
        startDateMonth = data['data']['startDateMonth']
        startDateDay = data['data']['startDateDay']
        endDateYear = data['data']['endDateYear']
        endDateMonth = data['data']['endDateMonth']
        endDateDay = data['data']['endDateDay']
       
        startDate = date(startDateYear,startDateMonth,startDateDay)
        endDate = date(endDateYear,endDateMonth,endDateDay)
        
        flow_stats = FlowAggregateStats.objects.filter(
            created__range=(startDate, endDate)
        ).order_by('-id')[:maxRecords]
        flow_stats_reversed = reversed(flow_stats)       
        serializer = FlowStatsSerializer(flow_stats_reversed, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

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

class AttackNotificationView(APIView):
    
    def get(self,request):
        attack_notification = AttackNotification.objects.order_by('-id')[:7]
        attack_notification_reversed = reversed(attack_notification)
        serializer = AttackNotificationSerializer(attack_notification_reversed, many=True)
        return Response(serializer.data)

class UpdateControllerIPView(APIView):
    def get(self,request):
        configuration_instance = ConfigurationModel.objects.get(id = 1)
        serializer = ConfigurationModelSerializer(configuration_instance)
        return Response(serializer.data)

    def post(self,request):
        # print(request.body)
        data = json.loads(request.body.decode('utf-8'))
        # print(data['data']['controllerIP'])
        try:
            configuration_instance = ConfigurationModel.objects.get(id = 1)
            configuration_instance.controllerIP = data['data']['controllerIP']
            configuration_instance.save()
            return Response(data=data["data"], status=status.HTTP_200_OK)
        except ConfigurationModel.DoesNotExist:
            # If entry doesn't exists, create a new one
            configuration_instance = ConfigurationModel.objects.create(
                 controllerIP = data['data']['controllerIP'], 
            )
            return Response(data=data["data"], status=status.HTTP_201_CREATED)

class UpdateMLView(APIView):
    def get(self,request):
        configuration_instance = ConfigurationModel.objects.get(id = 1)
        serializer = ConfigurationModelSerializer(configuration_instance)
        return Response(serializer.data)

    def post(self,request):
        data = json.loads(request.body.decode('utf-8'))
        try:
            configuration_instance = ConfigurationModel.objects.get(id = 1)
            configuration_instance.ml_threshold = data['data']['ml_threshold']
            configuration_instance.save()
            return Response(data=data["data"], status=status.HTTP_200_OK)
        except ConfigurationModel.DoesNotExist:
            # If entry doesn't exists, create a new one
            configuration_instance = ConfigurationModel.objects.create(
                 controllerIP = data['data']['ml_threshold'], 
            )
            return Response(data=data["data"], status=status.HTTP_201_CREATED)