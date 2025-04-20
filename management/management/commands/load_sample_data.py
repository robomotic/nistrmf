from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from map.models import AISystem, LifecycleStage, TrustworthinessCharacteristic, ImpactAssessment
from measure.models import Metric, Assessment, TEVV, EnvironmentalMetric, HumanAIEvaluation
from govern.models import Policy, Role, RiskAppetite, GovernanceStructure, GovernanceRole, HumanAIOversight, ThirdPartyRisk
from management.models import RiskResponse, Incident, ImprovementAction, PostDeploymentMonitoring, EmergentRisk
from django.utils import timezone

class Command(BaseCommand):
    help = 'Load sample data for NIST AI RMF models.'

    def handle(self, *args, **options):
        User = get_user_model()
        user, _ = User.objects.get_or_create(username='sampleuser', defaults={'email': 'sample@example.com'})

        # Lifecycle stages
        stage, _ = LifecycleStage.objects.get_or_create(name="Development", defaults={"description": "Development stage", "order": 1})

        # AI System
        ai, _ = AISystem.objects.get_or_create(
            name="Sample AI System",
            defaults={
                "description": "A sample AI system for demonstration.",
                "version": "1.0",
                "purpose": "Demo purposes",
                "deployment_status": "DEVELOPMENT",
                "owner": user,
                "lifecycle_stage": stage,
            }
        )

        # Trustworthiness
        for char, _ in TrustworthinessCharacteristic.CHARACTERISTICS:
            TrustworthinessCharacteristic.objects.get_or_create(
                ai_system=ai,
                characteristic=char,
                defaults={"score": 0.8, "notes": f"Sample score for {char}", "evaluated_by": user}
            )

        # Impact Assessment
        ImpactAssessment.objects.get_or_create(
            ai_system=ai,
            impact_type="INDIVIDUAL",
            defaults={"description": "Sample positive impact.", "positive": True, "assessed_by": user}
        )

        # Metric
        metric, _ = Metric.objects.get_or_create(
            name="Accuracy",
            ai_system=ai,
            defaults={
                "description": "Accuracy metric.",
                "unit": "%",
                "measurement_frequency": "Monthly",
                "collection_method": "Automated",
                "threshold_warning": 80.0,
                "threshold_critical": 60.0,
                "measurement_type": "QUANTITATIVE",
                "data_requirements": "Test set",
                "limitations": "None",
                "validation_method": "Cross-validation",
                "created_by": user
            }
        )

        # Assessment
        assessment, _ = Assessment.objects.get_or_create(
            ai_system=ai,
            assessment_type="INITIAL",
            defaults={
                "date_performed": timezone.now(),
                "performed_by": user,
                "findings": "All good.",
                "recommendations": "Proceed.",
                "assessment_methodology": "Manual review",
                "confidence_level": 0.9
            }
        )

        # TEVV
        TEVV.objects.get_or_create(
            ai_system=ai,
            defaults={
                "test_set_description": "Sample test set",
                "validation_method": "Manual",
                "verification_method": "Peer review",
                "evaluation_method": "Automated",
                "performance_criteria": ">80% accuracy",
                "performed_by": user
            }
        )

        # Environmental Metric
        EnvironmentalMetric.objects.get_or_create(
            ai_system=ai,
            metric_name="CO2 Emissions",
            defaults={"value": 10.5, "unit": "kg", "notes": "Sample metric"}
        )

        # Human-AI Evaluation
        HumanAIEvaluation.objects.get_or_create(
            ai_system=ai,
            assessment=assessment,
            defaults={
                "configuration": "Human-in-the-loop",
                "intervention_points": "Review stage",
                "oversight_mechanisms": "Manual override",
                "evaluated_by": user
            }
        )

        # Policy
        policy, _ = Policy.objects.get_or_create(
            title="Sample Policy",
            defaults={
                "description": "Sample policy desc.",
                "version": "1.0",
                "effective_date": timezone.now(),
                "last_reviewed": timezone.now(),
                "status": "ACTIVE",
                "created_by": user,
                "applicability": "All systems",
                "third_party_requirements": "Comply with standards",
                "review_process": "Annual",
                "exceptions_process": "Board approval",
                "compliance_requirements": "NIST",
                "lifecycle_integration": "All stages",
                "trustworthiness_requirements": "All"
            }
        )

        # Role
        role, _ = Role.objects.get_or_create(
            name="AI Lead",
            defaults={
                "description": "Leads AI projects.",
                "responsibilities": "Oversight",
                "oversight_areas": "All",
                "third_party_oversight": "Vendors",
                "escalation_path": "To board",
                "required_qualifications": "PhD",
                "delegation_authority": "Manager",
                "lifecycle_stages": "All",
                "trustworthiness_focus": "All"
            }
        )
        role.users.add(user)
        role.policies.add(policy)

        # Governance Structure
        gov_struct, _ = GovernanceStructure.objects.get_or_create(
            name="AI Board",
            defaults={
                "description": "Oversees AI.",
                "structure_type": "BOARD",
                "authority_level": "OVERSIGHT",
                "meeting_frequency": "Monthly",
                "charter": "Sample charter",
                "responsibilities": "Oversight"
            }
        )
        gov_struct.members.add(user)
        gov_struct.policies.add(policy)

        # Governance Role
        gov_role, _ = GovernanceRole.objects.get_or_create(
            name="AI Risk Officer",
            defaults={
                "description": "Manages risk.",
                "responsibilities": "Risk management",
                "lifecycle_stages": "All",
                "trustworthiness_focus": "All"
            }
        )
        gov_role.ai_systems.add(ai)

        # Human AI Oversight
        HumanAIOversight.objects.get_or_create(
            ai_system=ai,
            role=gov_role,
            defaults={
                "description": "Oversight desc.",
                "intervention_points": "Review",
                "oversight_mechanisms": "Manual"
            }
        )

        # Third Party Risk
        ThirdPartyRisk.objects.get_or_create(
            ai_system=ai,
            third_party_name="VendorX",
            defaults={
                "component_type": "SOFTWARE",
                "risk_description": "Dependency risk",
                "mitigation_measures": "Regular review",
                "monitoring_plan": "Annual",
                "last_reviewed": timezone.now()
            }
        )

        # Post Deployment Monitoring
        pdm, _ = PostDeploymentMonitoring.objects.get_or_create(
            ai_system=ai,
            defaults={
                "monitoring_plan": "Monitor outputs",
                "monitoring_metrics": "Accuracy, fairness",
                "feedback_mechanisms": "User feedback",
                "incident_response_plan": "Immediate response"
            }
        )

        # Emergent Risk
        erisk, _ = EmergentRisk.objects.get_or_create(
            ai_system=ai,
            defaults={
                "description": "New risk found",
                "detected_by": user,
                "mitigation_status": "OPEN"
            }
        )

        # Incident
        incident, _ = Incident.objects.get_or_create(
            ai_system=ai,
            title="Sample Incident",
            defaults={
                "description": "Incident desc.",
                "severity": "MEDIUM",
                "reported_by": user,
                "resolution": "Resolved",
                "lifecycle_stage": stage,
                "post_deployment_monitoring": pdm
            }
        )
        incident.emergent_risks.add(erisk)

        # Improvement Action
        ia, _ = ImprovementAction.objects.get_or_create(
            ai_system=ai,
            title="Sample Improvement",
            defaults={
                "description": "Improve process.",
                "source": "INCIDENT",
                "priority": "HIGH",
                "responsible": user,
                "status": "PROPOSED",
                "related_lifecycle_stage": stage
            }
        )
        ia.related_trustworthiness.set(TrustworthinessCharacteristic.objects.filter(ai_system=ai))

        self.stdout.write(self.style.SUCCESS('Sample data loaded.'))
