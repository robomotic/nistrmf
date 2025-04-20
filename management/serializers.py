from rest_framework import serializers
from .models import RiskResponse, Incident, ImprovementAction, PostDeploymentMonitoring, EmergentRisk

class RiskResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskResponse
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class ImprovementActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImprovementAction
        fields = '__all__'

class PostDeploymentMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDeploymentMonitoring
        fields = '__all__'

class EmergentRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergentRisk
        fields = '__all__'
