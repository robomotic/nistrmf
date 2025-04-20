from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from map.models import AISystem, RiskIdentification, LifecycleStage

def get_next_assessment_date():
    return timezone.now() + timedelta(days=90)

class Metric(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    unit = models.CharField(max_length=50)
    measurement_frequency = models.CharField(max_length=50)
    collection_method = models.TextField()
    threshold_warning = models.FloatField(help_text="Warning threshold value")
    threshold_critical = models.FloatField(help_text="Critical threshold value")
    measurement_type = models.CharField(max_length=50, choices=[
        ('QUANTITATIVE', 'Quantitative'),
        ('QUALITATIVE', 'Qualitative'),
        ('HYBRID', 'Hybrid')
    ])
    confidence_level = models.FloatField(help_text="Confidence level in measurement (0-1)", null=True, blank=True)
    data_requirements = models.TextField(help_text="Data required for measurement")
    limitations = models.TextField(help_text="Known limitations or constraints of the metric")
    third_party_dependencies = models.TextField(help_text="Third-party dependencies affecting measurement", blank=True)
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='metrics')
    related_risks = models.ManyToManyField(RiskIdentification, related_name='associated_metrics')
    validation_method = models.TextField(help_text="Method used to validate measurements")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.ai_system.name}"

class Assessment(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='assessments')
    assessment_type = models.CharField(max_length=100, choices=[
        ('INITIAL', 'Initial Assessment'),
        ('PERIODIC', 'Periodic Review'),
        ('INCIDENT', 'Post-Incident'),
        ('CHANGE', 'Change-Triggered')
    ])
    date_performed = models.DateField(default=timezone.now)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    findings = models.TextField()
    recommendations = models.TextField()
    next_assessment_date = models.DateField(default=get_next_assessment_date)
    assessment_methodology = models.TextField(help_text="Detailed description of assessment methodology")
    third_party_tools = models.TextField(help_text="Third-party tools or methodologies used", blank=True)
    confidence_level = models.FloatField(help_text="Confidence level in assessment (0-1)")
    limitations_encountered = models.TextField(help_text="Limitations encountered during assessment", blank=True)
    
    def __str__(self):
        return f"{self.ai_system.name} - {self.assessment_type} - {self.date_performed}"

class MetricMeasurement(models.Model):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='measurements')
    value = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[
        ('NORMAL', 'Normal'),
        ('WARNING', 'Warning'),
        ('CRITICAL', 'Critical')
    ])
    notes = models.TextField(blank=True)
    measurement_context = models.TextField(help_text="Contextual information about the measurement")
    data_sources = models.TextField(help_text="Sources of measurement data")
    confidence_score = models.FloatField(help_text="Confidence score for this measurement (0-1)", null=True)
    validation_status = models.CharField(max_length=50, choices=[
        ('PENDING', 'Pending Validation'),
        ('VALIDATED', 'Validated'),
        ('REJECTED', 'Validation Failed'),
        ('UNCERTAIN', 'Validation Uncertain')
    ])
    validation_notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.metric.name} - {self.value} - {self.timestamp}"
    
    def save(self, *args, **kwargs):
        if self.value >= self.metric.threshold_critical:
            self.status = 'CRITICAL'
        elif self.value >= self.metric.threshold_warning:
            self.status = 'WARNING'
        else:
            self.status = 'NORMAL'
        super().save(*args, **kwargs)

class TEVV(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='tevv_records')
    test_set_description = models.TextField()
    validation_method = models.TextField()
    verification_method = models.TextField()
    evaluation_method = models.TextField()
    performance_criteria = models.TextField()
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tevved_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"TEVV for {self.ai_system.name} at {self.tevved_at}"

class EnvironmentalMetric(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='environmental_metrics')
    metric_name = models.CharField(max_length=100)
    value = models.FloatField()
    unit = models.CharField(max_length=50)
    measured_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.metric_name} for {self.ai_system.name}"

class HumanAIEvaluation(models.Model):
    ai_system = models.ForeignKey(AISystem, on_delete=models.CASCADE, related_name='human_ai_evaluations')
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE, related_name='human_ai_evaluations')
    configuration = models.TextField(help_text="Describe human-AI teaming/configuration.")
    intervention_points = models.TextField(help_text="Describe human intervention points.")
    oversight_mechanisms = models.TextField(help_text="Describe oversight mechanisms.")
    evaluation_notes = models.TextField(blank=True)
    evaluated_at = models.DateTimeField(default=timezone.now)
    evaluated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Human-AI Evaluation for {self.ai_system.name}"
