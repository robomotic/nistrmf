from django.shortcuts import render
from rest_framework import viewsets
from .models import RiskResponse, Incident, ImprovementAction, PostDeploymentMonitoring, EmergentRisk
from .serializers import RiskResponseSerializer, IncidentSerializer, ImprovementActionSerializer, PostDeploymentMonitoringSerializer, EmergentRiskSerializer

# Create your views here.

class RiskResponseViewSet(viewsets.ModelViewSet):
    queryset = RiskResponse.objects.all()
    serializer_class = RiskResponseSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class ImprovementActionViewSet(viewsets.ModelViewSet):
    queryset = ImprovementAction.objects.all()
    serializer_class = ImprovementActionSerializer

class PostDeploymentMonitoringViewSet(viewsets.ModelViewSet):
    queryset = PostDeploymentMonitoring.objects.all()
    serializer_class = PostDeploymentMonitoringSerializer

class EmergentRiskViewSet(viewsets.ModelViewSet):
    queryset = EmergentRisk.objects.all()
    serializer_class = EmergentRiskSerializer
