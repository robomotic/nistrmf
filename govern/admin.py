from django.contrib import admin
from .models import Policy, Role, RiskAppetite, GovernanceStructure, ThirdPartyOversight, GovernanceRole, HumanAIOversight, ThirdPartyRisk

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'version', 'status', 'effective_date', 'last_reviewed')
    search_fields = ('title', 'description')
    list_filter = ('status', 'effective_date', 'last_reviewed')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    filter_horizontal = ('users', 'policies')

@admin.register(RiskAppetite)
class RiskAppetiteAdmin(admin.ModelAdmin):
    list_display = ('level', 'approved_date', 'review_frequency')
    list_filter = ('level', 'approved_date')

@admin.register(GovernanceRole)
class GovernanceRoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "description")

@admin.register(HumanAIOversight)
class HumanAIOversightAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "role", "created_at")
    search_fields = ("ai_system__name", "role__name")

@admin.register(ThirdPartyRisk)
class ThirdPartyRiskAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "third_party_name", "component_type", "last_reviewed")
    search_fields = ("ai_system__name", "third_party_name")
