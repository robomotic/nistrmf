from django.shortcuts import render
from rest_framework import viewsets
from .models import Policy, Role, RiskAppetite, GovernanceStructure, ThirdPartyOversight, GovernanceRole, HumanAIOversight, ThirdPartyRisk
from .serializers import PolicySerializer, RoleSerializer, RiskAppetiteSerializer, GovernanceStructureSerializer, ThirdPartyOversightSerializer, GovernanceRoleSerializer, HumanAIOversightSerializer, ThirdPartyRiskSerializer

# Create your views here.

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RiskAppetiteViewSet(viewsets.ModelViewSet):
    queryset = RiskAppetite.objects.all()
    serializer_class = RiskAppetiteSerializer

class GovernanceRoleViewSet(viewsets.ModelViewSet):
    queryset = GovernanceRole.objects.all()
    serializer_class = GovernanceRoleSerializer

class HumanAIOversightViewSet(viewsets.ModelViewSet):
    queryset = HumanAIOversight.objects.all()
    serializer_class = HumanAIOversightSerializer

class ThirdPartyRiskViewSet(viewsets.ModelViewSet):
    queryset = ThirdPartyRisk.objects.all()
    serializer_class = ThirdPartyRiskSerializer
