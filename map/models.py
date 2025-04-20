from django.db import models
from django.contrib.auth.models import User
from govern.models import RiskAppetite
from django.utils import timezone

class LifecycleStage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class TrustworthinessCharacteristic(models.Model):
    CHARACTERISTICS = [
        ("VALID_RELIABLE", "Valid & Reliable"),
        ("SAFE", "Safe"),
        ("SECURE_RESILIENT", "Secure & Resilient"),
        ("ACCOUNTABLE_TRANSPARENT", "Accountable & Transparent"),
        ("EXPLAINABLE_INTERPRETABLE", "Explainable & Interpretable"),
        ("PRIVACY_ENHANCED", "Privacy-Enhanced"),
        ("FAIR_BIAS_MANAGED", "Fair with Harmful Bias Managed"),
    ]
    ai_system = models.ForeignKey('AISystem', on_delete=models.CASCADE, related_name='trustworthiness_evaluations')
    characteristic = models.CharField(max_length=40, choices=CHARACTERISTICS)
    score = models.FloatField(help_text="0-1 scale or qualitative score")
    notes = models.TextField(blank=True)
    evaluated_at = models.DateTimeField(default=timezone.now)
    evaluated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_characteristic_display()} for {self.ai_system.name}"

class ImpactAssessment(models.Model):
    IMPACT_TYPE = [
        ("INDIVIDUAL", "Individual"),
        ("GROUP", "Group/Community"),
        ("SOCIETAL", "Societal"),
        ("ORGANIZATION", "Organization"),
        ("ECOSYSTEM", "Ecosystem"),
        ("ENVIRONMENT", "Environment/Planet"),
    ]
    ai_system = models.ForeignKey('AISystem', on_delete=models.CASCADE, related_name='impact_assessments')
    impact_type = models.CharField(max_length=20, choices=IMPACT_TYPE)
    description = models.TextField()
    positive = models.BooleanField()
    assessed_at = models.DateTimeField(default=timezone.now)
    assessed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_impact_type_display()} impact for {self.ai_system.name}"

class AISystem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    version = models.CharField(max_length=50)
    purpose = models.TextField()
    deployment_status = models.CharField(max_length=50, choices=[
        ('DEVELOPMENT', 'In Development'),
        ('TESTING', 'Testing'),
        ('PRODUCTION', 'Production'),
        ('RETIRED', 'Retired')
    ])
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owned_systems')
    risk_appetite = models.ForeignKey(RiskAppetite, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    third_party_components = models.TextField(help_text="List of third-party software, hardware, and data dependencies")
    governance_structure = models.TextField(help_text="Internal governance structures and technical safeguards")
    lifecycle_stage = models.ForeignKey(LifecycleStage, on_delete=models.SET_NULL, null=True, blank=True)
    version_history = models.TextField(blank=True, help_text="Describe version changes and transitions.")
    human_roles = models.TextField(blank=True, help_text="Describe human roles and responsibilities in oversight.")
    human_intervention_points = models.TextField(blank=True, help_text="Describe where/when humans intervene.")
    environmental_impact = models.TextField(blank=True, help_text="Describe computational/environmental impact.")

    def __str__(self):
        return f"{self.name} - v{self.version}"

class Context(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='contexts')
    domain = models.CharField(max_length=100)
    intended_use = models.TextField()
    constraints = models.TextField()
    assumptions = models.TextField()
    dependencies = models.TextField()
    stakeholders = models.TextField()
    impact_areas = models.TextField()

    class Meta:
        verbose_name_plural = "Contexts"

    def __str__(self):
        return f"{self.ai_system.name} - {self.domain}"

class RiskIdentification(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='risks')
    risk_type = models.CharField(max_length=100)
    description = models.TextField()
    likelihood = models.CharField(max_length=50, choices=[
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High')
    ])
    impact = models.CharField(max_length=50, choices=[
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical')
    ])
    identified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    identified_date = models.DateField(auto_now_add=True)
    last_assessed = models.DateField(auto_now=True)
    mitigation_status = models.CharField(max_length=50, choices=[
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('MITIGATED', 'Mitigated'),
        ('ACCEPTED', 'Accepted')
    ])
    risk_category = models.CharField(max_length=50, choices=[
        ('INTERNAL', 'Internal System Risk'),
        ('THIRD_PARTY', 'Third-Party Component Risk'),
        ('EMERGENT', 'Emergent Risk'),
        ('INTEGRATION', 'Integration Risk')
    ])
    risk_source = models.CharField(max_length=50, choices=[
        ('SOFTWARE', 'Software'),
        ('HARDWARE', 'Hardware'),
        ('DATA', 'Data'),
        ('PROCESS', 'Process'),
        ('HUMAN', 'Human Factor')
    ])
    measurement_methodology = models.TextField(help_text="Description of risk measurement approach and metrics")
    tracking_frequency = models.CharField(max_length=50, choices=[
        ('CONTINUOUS', 'Continuous'),
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('QUARTERLY', 'Quarterly')
    ])
    related_risks = models.ManyToManyField('self', blank=True, symmetrical=False,
                                         related_name='influenced_by')

    def __str__(self):
        return f"{self.ai_system.name} - {self.risk_type}"
