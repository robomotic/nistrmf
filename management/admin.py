from django.contrib import admin
from .models import RiskResponse, Incident, ImprovementAction, PostDeploymentMonitoring, EmergentRisk

@admin.register(RiskResponse)
class RiskResponseAdmin(admin.ModelAdmin):
    list_display = ('risk', 'response_type', 'responsible', 'deadline', 'status')
    search_fields = ('description', 'action_plan')
    list_filter = ('response_type', 'status', 'deadline')

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "title", "severity", "reported_by", "reported_date", "resolved_date", "lifecycle_stage")
    search_fields = ("title", "description", "resolution")
    list_filter = ("severity", "reported_date", "resolved_date", "lifecycle_stage")
    filter_horizontal = ("related_measurements", "related_risks", "trustworthiness_characteristics", "emergent_risks")

@admin.register(ImprovementAction)
class ImprovementActionAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "title", "source", "priority", "status", "target_date", "related_lifecycle_stage")
    search_fields = ("title", "description")
    list_filter = ("source", "priority", "status", "related_lifecycle_stage")
    filter_horizontal = ("related_trustworthiness",)

@admin.register(PostDeploymentMonitoring)
class PostDeploymentMonitoringAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "created_at")
    search_fields = ("ai_system__name",)

@admin.register(EmergentRisk)
class EmergentRiskAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "mitigation_status", "detected_at", "detected_by")
    search_fields = ("ai_system__name", "description")
