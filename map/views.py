from django.shortcuts import render
from rest_framework import viewsets
from .models import AISystem, Context, RiskIdentification, LifecycleStage, TrustworthinessCharacteristic, ImpactAssessment
from .serializers import AISystemSerializer, ContextSerializer, RiskIdentificationSerializer, LifecycleStageSerializer, TrustworthinessCharacteristicSerializer, ImpactAssessmentSerializer

# Create your views here.

class AISystemViewSet(viewsets.ModelViewSet):
    queryset = AISystem.objects.all()
    serializer_class = AISystemSerializer

class ContextViewSet(viewsets.ModelViewSet):
    queryset = Context.objects.all()
    serializer_class = ContextSerializer

class RiskIdentificationViewSet(viewsets.ModelViewSet):
    queryset = RiskIdentification.objects.all()
    serializer_class = RiskIdentificationSerializer

class LifecycleStageViewSet(viewsets.ModelViewSet):
    queryset = LifecycleStage.objects.all()
    serializer_class = LifecycleStageSerializer

class TrustworthinessCharacteristicViewSet(viewsets.ModelViewSet):
    queryset = TrustworthinessCharacteristic.objects.all()
    serializer_class = TrustworthinessCharacteristicSerializer

class ImpactAssessmentViewSet(viewsets.ModelViewSet):
    queryset = ImpactAssessment.objects.all()
    serializer_class = ImpactAssessmentSerializer
