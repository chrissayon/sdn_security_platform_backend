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
from datetime import datetime
from django.utils.timezone import make_aware
from django.utils import timezone
import pytz
from django.conf import settings
from itertools import chain

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
       
        startDate = datetime(startDateYear, startDateMonth, startDateDay)
        endDate = datetime(endDateYear, endDateMonth, endDateDay)

        awareStartDate = make_aware(startDate, timezone=pytz.timezone("Australia/Melbourne"))
        awareEndDate = make_aware(endDate, timezone=pytz.timezone("Australia/Melbourne"))

        flow_stats = FlowAggregateStats.objects.filter(
            created__range=(awareStartDate, awareEndDate)
        ).order_by('-id')[:maxRecords]
        
        # print(startDate.tzinfo)

        serializer = FlowStatsSerializer(flow_stats, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class PortStatsView(APIView):

    def get(self, request):
        '''Obtain all port statistics from database'''
        port_stats = PortStats.objects.order_by('-id')[:100]
        port_stats_reversed = reversed(port_stats)
        serializer = PortStatsSerializer(port_stats, many=True)
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
       
        startDate = datetime(startDateYear, startDateMonth, startDateDay)
        endDate = datetime(endDateYear, endDateMonth, endDateDay)

        awareStartDate = make_aware(startDate, timezone=pytz.timezone("Australia/Melbourne"))
        awareEndDate = make_aware(endDate, timezone=pytz.timezone("Australia/Melbourne"))
        
        port_no = data['data']['port_no']
  
        if port_no == 'All':
            port_stats = PortStats.objects.filter(
                created__range=(awareStartDate, awareEndDate)
            ).order_by('-id')[:maxRecords]
        else:
            port_stats = PortStats.objects.filter(
                created__range=(awareStartDate, awareEndDate)
            ).filter(port_no=port_no).order_by('-id')[:maxRecords]
          
        serializer = PortStatsSerializer(port_stats, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FlowAggregateDiffStatsView(APIView):

    def get(self, request):
        '''Get the flow aggregate statistics difference'''
        flow_agg_diff_stats = FlowAggregateDiffStats.objects.order_by('-id')[:7]
        flow_agg_diff_stats_reversed = reversed(flow_agg_diff_stats)
        serializer = FlowAggregateDiffStatsSerializer(flow_agg_diff_stats_reversed, many=True)
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
       
        startDate = datetime(startDateYear, startDateMonth, startDateDay)
        endDate = datetime(endDateYear, endDateMonth, endDateDay)

        awareStartDate = make_aware(startDate, timezone=pytz.timezone("Australia/Melbourne"))
        awareEndDate = make_aware(endDate, timezone=pytz.timezone("Australia/Melbourne"))

        
        flow_agg_diff_stats = FlowAggregateDiffStats.objects.filter(
            created__range=(awareStartDate, awareEndDate)
        ).order_by('-id')[:maxRecords]
          

        serializer = FlowAggregateDiffStatsSerializer(flow_agg_diff_stats, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PortDiffStatsView(APIView):

    def get(self, request):
        '''Get the port statistics difference'''
        #latest_port_stats = PortStats.objects.order_by('id').reverse()[1]
        port_diff_stats = PortDiffStats.objects.filter(port_no = 3).order_by('-id')[:7]
        port_diff_stats_reversed = reversed(port_diff_stats)
        serializer = PortDiffStatsSerializer(port_diff_stats_reversed, many=True)
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
       
        startDate = datetime(startDateYear, startDateMonth, startDateDay)
        endDate = datetime(endDateYear, endDateMonth, endDateDay)

        awareStartDate = make_aware(startDate, timezone=pytz.timezone("Australia/Melbourne"))
        awareEndDate = make_aware(endDate, timezone=pytz.timezone("Australia/Melbourne"))

        port_no = data['data']['port_no']
  
        if port_no == 'All':
            port_diff_stats = PortDiffStats.objects.filter(
                created__range=(awareStartDate, awareEndDate)
            ).order_by('-id')[:maxRecords]
        else:
            port_diff_stats = PortDiffStats.objects.filter(
                created__range=(awareStartDate, awareEndDate)
            ).filter(port_no=port_no).order_by('-id')[:maxRecords]
        
       
          
        serializer = PortDiffStatsSerializer(port_diff_stats, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class AttackNotificationView(APIView):
    
    def get(self,request):
        attack_notification = AttackNotification.objects.order_by('-id')[:7]
        attack_notification_reversed = reversed(attack_notification)
        serializer = AttackNotificationSerializer(attack_notification_reversed, many=True)
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
       
        startDate = datetime(startDateYear, startDateMonth, startDateDay)
        endDate = datetime(endDateYear, endDateMonth, endDateDay)
        
        awareStartDate = make_aware(startDate, timezone=pytz.timezone("Australia/Melbourne"))
        awareEndDate = make_aware(endDate, timezone=pytz.timezone("Australia/Melbourne"))

        attack_notification = AttackNotification.objects.filter(
            created__range=(awareStartDate, awareEndDate)
        ).order_by('-id')[:maxRecords]
          
        serializer = AttackNotificationSerializer(attack_notification, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


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
        print(data['data'])
        try:
            configuration_instance = ConfigurationModel.objects.get(id = 1)
            configuration_instance.ml_threshold = data['data']['ml_threshold']
            configuration_instance.port_threshold = data['data']['port_threshold']
            configuration_instance.port_diff_threshold = data['data']['port_diff_threshold']
            configuration_instance.flow_aggregate_threshold = data['data']['flow_aggregate_threshold']
            configuration_instance.flow_aggregate_difference_threshold = data['data']['flow_aggregate_difference_threshold']
            configuration_instance.save()
            return Response(data=data["data"], status=status.HTTP_200_OK)
        except ConfigurationModel.DoesNotExist:
            # If entry doesn't exists, create a new one
            configuration_instance = ConfigurationModel.objects.create(
                ml_threshold = data['data']['ml_threshold'], 
                port_threshold = data['data']['port_threshold'],
                port_diff_threshold = data['data']['port_diff_threshold'],
                flow_aggregate_threshold = data['data']['flow_aggregate_threshold'],
                flow_aggregate_difference_threshold = data['data']['flow_aggregate_difference_threshold'],
            )
            return Response(data=data["data"], status=status.HTTP_201_CREATED)

# class UpdateThresholdStatsView(APIView):
#     def get(self,request):
#         configuration_instance = ConfigurationModel.objects.get(id = 1)
#         serializer = ConfigurationModelSerializer(configuration_instance)
#         return Response(serializer.data)

#     def post(self,request):
#         data = json.loads(request.body.decode('utf-8'))
#         try:
#             configuration_instance = ConfigurationModel.objects.get(id = 1)
#             configuration_instance.flow_aggregate_threshold = data['data']['flow_aggregate_threshold']
#             configuration_instance.save()
#             return Response(data=data["data"], status=status.HTTP_200_OK)
#         except ConfigurationModel.DoesNotExist:
#             # If entry doesn't exists, create a new one
#             configuration_instance = ConfigurationModel.objects.create(
#                  flow_aggregate_threshold = data['data']['flow_aggregate_threshold'], 
#             )
#             return Response(data=data["data"], status=status.HTTP_201_CREATED)



class PortGraphView(APIView):
    def get(self, request):
        '''Get port data for graphing'''
        port_stats_1 = PortStats.objects.filter(port_no='1').order_by('-id')[:1]
        port_stats_2 = PortStats.objects.filter(port_no='2').order_by('-id')[:1]
        port_stats_3 = PortStats.objects.filter(port_no='3').order_by('-id')[:1]
        port_stats_LOCAL = PortStats.objects.filter(port_no='LOCAL').order_by('-id')[:1]
        port_stats_result = list(chain(port_stats_1, port_stats_2, port_stats_3, port_stats_LOCAL))
        serializer = PortStatsSerializer(port_stats_result)
        return Response(serializer.data)

    def post(self, request):
        '''Post port data for graphing'''
        data = json.loads(request.body.decode('utf-8'))
        
        maxRecords = data['data']['maxRecords']
        port_stats_1 = PortStats.objects.filter(port_no='1').order_by('-id')[:maxRecords]
        port_stats_2 = PortStats.objects.filter(port_no='2').order_by('-id')[:maxRecords]
        port_stats_3 = PortStats.objects.filter(port_no='3').order_by('-id')[:maxRecords]
        port_stats_LOCAL = PortStats.objects.filter(port_no='LOCAL').order_by('-id')[:maxRecords]
        port_stats_result = list(chain(port_stats_1, port_stats_2, port_stats_3, port_stats_LOCAL))
        serializer = PortStatsSerializer(port_stats_result, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class PortDiffGraphView(APIView):
    def get(self, request):
        '''Get the port statistics difference'''
        #latest_port_stats = PortStats.objects.order_by('id').reverse()[1]
        port_diff_stats_1 = PortDiffStats.objects.filter(port_no='1').order_by('-id')[:1]
        port_diff_stats_2 = PortDiffStats.objects.filter(port_no='2').order_by('-id')[:1]
        port_diff_stats_3 = PortDiffStats.objects.filter(port_no='3').order_by('-id')[:1]
        port_diff_stats_LOCAL = PortDiffStats.objects.filter(port_no='LOCAL').order_by('-id')[:1]
        port_diff_result = list(chain(port_diff_stats_1, port_diff_stats_2, port_diff_stats_3, port_diff_stats_LOCAL))
        serializer = PortDiffStatsSerializer(port_diff_result, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        '''Obtain flow aggregate statistics from database'''
        data = json.loads(request.body.decode('utf-8'))
        maxRecords = data['data']['maxRecords']

        port_diff_stats_1 = PortDiffStats.objects.filter(port_no='1').order_by('-id')[:maxRecords]
        port_diff_stats_2 = PortDiffStats.objects.filter(port_no='2').order_by('-id')[:maxRecords]
        port_diff_stats_3 = PortDiffStats.objects.filter(port_no='3').order_by('-id')[:maxRecords]
        port_diff_stats_LOCAL = PortDiffStats.objects.filter(port_no='LOCAL').order_by('-id')[:maxRecords]
        port_diff_result = list(chain(port_diff_stats_1, port_diff_stats_2, port_diff_stats_3, port_diff_stats_LOCAL))
        serializer = PortDiffStatsSerializer(port_diff_result, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




class FlowAggregateDiffGraphView(APIView):

    def get(self, request):
        '''Get the flow aggregate statistics difference'''
        flow_agg_diff_stats = FlowAggregateDiffStats.objects.last()
        serializer = FlowAggregateDiffStatsSerializer(flow_agg_diff_stats)
        return Response(serializer.data)
    
    def post(self, request):
        '''Obtain flow aggregate statistics from database'''
        data = json.loads(request.body.decode('utf-8'))
        maxRecords = data['data']['maxRecords']
        flow_agg_diff_stats = FlowAggregateDiffStats.objects.order_by('-id')[:maxRecords]

        serializer = FlowAggregateDiffStatsSerializer(flow_agg_diff_stats, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)