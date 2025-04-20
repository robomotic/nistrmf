from django.shortcuts import render
from rest_framework import viewsets
from .models import Metric, Assessment, MetricMeasurement, TEVV, EnvironmentalMetric, HumanAIEvaluation
from .serializers import MetricSerializer, AssessmentSerializer, MetricMeasurementSerializer, TEVVSerializer, EnvironmentalMetricSerializer, HumanAIEvaluationSerializer

# Create your views here.

class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class MetricMeasurementViewSet(viewsets.ModelViewSet):
    queryset = MetricMeasurement.objects.all()
    serializer_class = MetricMeasurementSerializer

class TEVVViewSet(viewsets.ModelViewSet):
    queryset = TEVV.objects.all()
    serializer_class = TEVVSerializer

class EnvironmentalMetricViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentalMetric.objects.all()
    serializer_class = EnvironmentalMetricSerializer

class HumanAIEvaluationViewSet(viewsets.ModelViewSet):
    queryset = HumanAIEvaluation.objects.all()
    serializer_class = HumanAIEvaluationSerializer
