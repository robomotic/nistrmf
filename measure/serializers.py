from rest_framework import serializers
from .models import Metric, Assessment, MetricMeasurement, TEVV, EnvironmentalMetric, HumanAIEvaluation

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class MetricMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricMeasurement
        fields = '__all__'

class TEVVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TEVV
        fields = '__all__'

class EnvironmentalMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalMetric
        fields = '__all__'

class HumanAIEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanAIEvaluation
        fields = '__all__'
