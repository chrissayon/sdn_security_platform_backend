from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DescStats
from .serializers import DescStatsSerializer

# List switch hardware description
class DescStatsView(APIView):

    def get(self, request):
        descstats = DescStats.objects.all()
        serializer = DescStatsSerializer(descstats, many=True)
        print(serializer.data)
        return Response(serializer.data)