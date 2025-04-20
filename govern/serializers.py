from rest_framework import serializers
from .models import Policy, Role, RiskAppetite, GovernanceRole, HumanAIOversight, ThirdPartyRisk, GovernanceStructure, ThirdPartyOversight

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class RiskAppetiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskAppetite
        fields = '__all__'

class GovernanceRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceRole
        fields = '__all__'

class HumanAIOversightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanAIOversight
        fields = '__all__'

class ThirdPartyRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdPartyRisk
        fields = '__all__'

class GovernanceStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceStructure
        fields = '__all__'

class ThirdPartyOversightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdPartyOversight
        fields = '__all__'
