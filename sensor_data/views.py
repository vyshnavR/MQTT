from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

def dashboard(request):    
    data = SensorData.objects.order_by('-timestamp')[:20]
    return render(request, 'dashboard.html', {'data': data})


class FilteredSensorView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'data_table.html'

    def get(self, request):
        queryset = SensorData.objects.all()
        device_id = request.GET.get('device_id')
        ordering = request.GET.get('ordering', '-timestamp')

        if device_id:
            queryset = queryset.filter(device_id=device_id)
        queryset = queryset.order_by(ordering)

        return Response({'data': queryset})


class SensorDataListAPIView(generics.ListAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['device_id']  
    ordering_fields = ['timestamp'] 