from rest_framework import serializers
from .models import AISystem, Context, RiskIdentification, LifecycleStage, TrustworthinessCharacteristic, ImpactAssessment

class AISystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AISystem
        fields = '__all__'

class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = '__all__'

class RiskIdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskIdentification
        fields = '__all__'

class LifecycleStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifecycleStage
        fields = '__all__'

class TrustworthinessCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustworthinessCharacteristic
        fields = '__all__'

class ImpactAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactAssessment
        fields = '__all__'
