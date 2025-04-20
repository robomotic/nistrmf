from django.contrib import admin
from .models import Metric, Assessment, MetricMeasurement, TEVV, EnvironmentalMetric, HumanAIEvaluation

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('name', 'ai_system', 'unit', 'measurement_frequency')
    search_fields = ('name', 'description', 'collection_method')
    list_filter = ('measurement_frequency', 'created_at')

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('ai_system', 'assessment_type', 'date_performed', 'performed_by', 'next_assessment_date')
    search_fields = ('findings', 'recommendations')
    list_filter = ('assessment_type', 'date_performed')

@admin.register(MetricMeasurement)
class MetricMeasurementAdmin(admin.ModelAdmin):
    list_display = ('metric', 'value', 'status', 'timestamp')
    search_fields = ('notes',)
    list_filter = ('status', 'timestamp')

@admin.register(TEVV)
class TEVVAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "tevved_at", "performed_by")
    search_fields = ("ai_system__name", "test_set_description")

@admin.register(EnvironmentalMetric)
class EnvironmentalMetricAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "metric_name", "value", "unit", "measured_at")
    search_fields = ("ai_system__name", "metric_name")

@admin.register(HumanAIEvaluation)
class HumanAIEvaluationAdmin(admin.ModelAdmin):
    list_display = ("ai_system", "assessment", "evaluated_at", "evaluated_by")
    search_fields = ("ai_system__name", "configuration")
