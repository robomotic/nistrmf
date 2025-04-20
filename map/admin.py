from django.contrib import admin
from .models import AISystem, Context, RiskIdentification, LifecycleStage, TrustworthinessCharacteristic, ImpactAssessment

@admin.register(AISystem)
class AISystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'deployment_status', 'owner')
    search_fields = ('name', 'description', 'purpose')
    list_filter = ('deployment_status', 'created_at')

@admin.register(Context)
class ContextAdmin(admin.ModelAdmin):
    list_display = ('ai_system', 'domain', 'intended_use')
    search_fields = ('domain', 'intended_use', 'constraints')
    list_filter = ('domain',)

@admin.register(RiskIdentification)
class RiskIdentificationAdmin(admin.ModelAdmin):
    list_display = ('ai_system', 'risk_type', 'likelihood', 'impact', 'mitigation_status')
    search_fields = ('risk_type', 'description')
    list_filter = ('likelihood', 'impact', 'mitigation_status')

@admin.register(LifecycleStage)
class LifecycleStageAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    search_fields = ("name",)

@admin.register(TrustworthinessCharacteristic)
class TrustworthinessCharacteristicAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "characteristic", "score", "evaluated_at", "evaluated_by")
    list_filter = ("characteristic",)
    search_fields = ("ai_system__name", "notes")

@admin.register(ImpactAssessment)
class ImpactAssessmentAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "impact_type", "positive", "assessed_at", "assessed_by")
    list_filter = ("impact_type", "positive")
    search_fields = ("ai_system__name", "description")
