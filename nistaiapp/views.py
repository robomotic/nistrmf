from django.shortcuts import render
from map.models import AISystem, LifecycleStage, TrustworthinessCharacteristic, ImpactAssessment
from measure.models import Assessment, TEVV, EnvironmentalMetric, HumanAIEvaluation
from govern.models import Policy, Role, RiskAppetite, GovernanceStructure, GovernanceRole, HumanAIOversight, ThirdPartyRisk
from management.models import Incident, ImprovementAction, PostDeploymentMonitoring, EmergentRisk

def main_dashboard(request):
    context = {
        'ai_systems': AISystem.objects.all(),
        'lifecycle_stages': LifecycleStage.objects.all(),
        'trustworthiness': TrustworthinessCharacteristic.objects.all(),
        'impact_assessments': ImpactAssessment.objects.all(),
        'assessments': Assessment.objects.all(),
        'tevv': TEVV.objects.all(),
        'environmental_metrics': EnvironmentalMetric.objects.all(),
        'human_ai_evaluations': HumanAIEvaluation.objects.all(),
        'policies': Policy.objects.all(),
        'roles': Role.objects.all(),
        'risk_appetites': RiskAppetite.objects.all(),
        'governance_structures': GovernanceStructure.objects.all(),
        'governance_roles': GovernanceRole.objects.all(),
        'human_ai_oversight': HumanAIOversight.objects.all(),
        'third_party_risks': ThirdPartyRisk.objects.all(),
        'incidents': Incident.objects.all(),
        'improvement_actions': ImprovementAction.objects.all(),
        'post_deployment_monitoring': PostDeploymentMonitoring.objects.all(),
        'emergent_risks': EmergentRisk.objects.all(),
    }
    return render(request, 'main_dashboard.html', context)
