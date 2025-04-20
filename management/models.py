from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from map.models import AISystem, RiskIdentification, LifecycleStage, TrustworthinessCharacteristic
from measure.models import Assessment, MetricMeasurement

def get_default_deadline():
    return timezone.now() + timedelta(days=30)

def get_default_target_date():
    return timezone.now() + timedelta(days=60)

class RiskResponse(models.Model):
    risk = models.ForeignKey(RiskIdentification, on_delete=models.CASCADE, related_name='responses')
    response_type = models.CharField(max_length=50, choices=[
        ('AVOID', 'Avoid Risk'),
        ('MITIGATE', 'Mitigate Risk'),
        ('TRANSFER', 'Transfer Risk'),
        ('ACCEPT', 'Accept Risk')
    ])
    description = models.TextField()
    action_plan = models.TextField()
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    deadline = models.DateField(default=get_default_deadline)
    status = models.CharField(max_length=50, choices=[
        ('PLANNED', 'Planned'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('BLOCKED', 'Blocked')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.risk.ai_system.name} - {self.response_type}"

class PostDeploymentMonitoring(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='post_deployment_monitoring')
    monitoring_plan = models.TextField()
    monitoring_metrics = models.TextField()
    feedback_mechanisms = models.TextField()
    incident_response_plan = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Monitoring for {self.ai_system.name}"

class EmergentRisk(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='emergent_risks')
    description = models.TextField()
    detected_at = models.DateTimeField(default=timezone.now)
    detected_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mitigation_status = models.CharField(max_length=50, choices=[
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('MITIGATED', 'Mitigated'),
        ('ACCEPTED', 'Accepted')
    ])
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Emergent risk for {self.ai_system.name}"

class Incident(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='incidents')
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=50, choices=[
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical')
    ])
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reported_incidents')
    reported_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    resolution = models.TextField(blank=True)
    related_measurements = models.ManyToManyField(MetricMeasurement, blank=True)
    related_risks = models.ManyToManyField(RiskIdentification, blank=True)
    lifecycle_stage = models.ForeignKey(LifecycleStage, on_delete=models.SET_NULL, null=True, blank=True)
    trustworthiness_characteristics = models.ManyToManyField(TrustworthinessCharacteristic, blank=True)
    post_deployment_monitoring = models.ForeignKey(PostDeploymentMonitoring, on_delete=models.SET_NULL, null=True, blank=True)
    emergent_risks = models.ManyToManyField(EmergentRisk, blank=True)

    def __str__(self):
        return f"{self.ai_system.name} - {self.title}"

class ImprovementAction(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='improvements')
    title = models.CharField(max_length=200)
    description = models.TextField()
    source = models.CharField(max_length=50, choices=[
        ('ASSESSMENT', 'Assessment Finding'),
        ('INCIDENT', 'Incident Response'),
        ('METRIC', 'Metric Analysis'),
        ('STAKEHOLDER', 'Stakeholder Feedback')
    ])
    priority = models.CharField(max_length=50, choices=[
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High')
    ])
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[
        ('PROPOSED', 'Proposed'),
        ('APPROVED', 'Approved'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    target_date = models.DateField(default=get_default_target_date)
    completed_date = models.DateField(null=True, blank=True)
    related_assessment = models.ForeignKey(Assessment, on_delete=models.SET_NULL, null=True, blank=True)
    related_incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
    related_lifecycle_stage = models.ForeignKey(LifecycleStage, on_delete=models.SET_NULL, null=True, blank=True)
    related_trustworthiness = models.ManyToManyField(TrustworthinessCharacteristic, blank=True)

    def __str__(self):
        return f"{self.ai_system.name} - {self.title}"
