# Generated by Django 5.2 on 2025-04-19 14:14

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('govern', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LifecycleStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AISystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('version', models.CharField(max_length=50)),
                ('purpose', models.TextField()),
                ('deployment_status', models.CharField(choices=[('DEVELOPMENT', 'In Development'), ('TESTING', 'Testing'), ('PRODUCTION', 'Production'), ('RETIRED', 'Retired')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('third_party_components', models.TextField(help_text='List of third-party software, hardware, and data dependencies')),
                ('governance_structure', models.TextField(help_text='Internal governance structures and technical safeguards')),
                ('version_history', models.TextField(blank=True, help_text='Describe version changes and transitions.')),
                ('human_roles', models.TextField(blank=True, help_text='Describe human roles and responsibilities in oversight.')),
                ('human_intervention_points', models.TextField(blank=True, help_text='Describe where/when humans intervene.')),
                ('environmental_impact', models.TextField(blank=True, help_text='Describe computational/environmental impact.')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owned_systems', to=settings.AUTH_USER_MODEL)),
                ('risk_appetite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='govern.riskappetite')),
                ('lifecycle_stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.lifecyclestage')),
            ],
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100)),
                ('intended_use', models.TextField()),
                ('constraints', models.TextField()),
                ('assumptions', models.TextField()),
                ('dependencies', models.TextField()),
                ('stakeholders', models.TextField()),
                ('impact_areas', models.TextField()),
                ('ai_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contexts', to='map.aisystem')),
            ],
            options={
                'verbose_name_plural': 'Contexts',
            },
        ),
        migrations.CreateModel(
            name='ImpactAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impact_type', models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('GROUP', 'Group/Community'), ('SOCIETAL', 'Societal'), ('ORGANIZATION', 'Organization'), ('ECOSYSTEM', 'Ecosystem'), ('ENVIRONMENT', 'Environment/Planet')], max_length=20)),
                ('description', models.TextField()),
                ('positive', models.BooleanField()),
                ('assessed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('ai_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impact_assessments', to='map.aisystem')),
                ('assessed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RiskIdentification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('likelihood', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=50)),
                ('impact', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('CRITICAL', 'Critical')], max_length=50)),
                ('identified_date', models.DateField(auto_now_add=True)),
                ('last_assessed', models.DateField(auto_now=True)),
                ('mitigation_status', models.CharField(choices=[('OPEN', 'Open'), ('IN_PROGRESS', 'In Progress'), ('MITIGATED', 'Mitigated'), ('ACCEPTED', 'Accepted')], max_length=50)),
                ('risk_category', models.CharField(choices=[('INTERNAL', 'Internal System Risk'), ('THIRD_PARTY', 'Third-Party Component Risk'), ('EMERGENT', 'Emergent Risk'), ('INTEGRATION', 'Integration Risk')], max_length=50)),
                ('risk_source', models.CharField(choices=[('SOFTWARE', 'Software'), ('HARDWARE', 'Hardware'), ('DATA', 'Data'), ('PROCESS', 'Process'), ('HUMAN', 'Human Factor')], max_length=50)),
                ('measurement_methodology', models.TextField(help_text='Description of risk measurement approach and metrics')),
                ('tracking_frequency', models.CharField(choices=[('CONTINUOUS', 'Continuous'), ('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly'), ('QUARTERLY', 'Quarterly')], max_length=50)),
                ('ai_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risks', to='map.aisystem')),
                ('identified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('related_risks', models.ManyToManyField(blank=True, related_name='influenced_by', to='map.riskidentification')),
            ],
        ),
        migrations.CreateModel(
            name='TrustworthinessCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristic', models.CharField(choices=[('VALID_RELIABLE', 'Valid & Reliable'), ('SAFE', 'Safe'), ('SECURE_RESILIENT', 'Secure & Resilient'), ('ACCOUNTABLE_TRANSPARENT', 'Accountable & Transparent'), ('EXPLAINABLE_INTERPRETABLE', 'Explainable & Interpretable'), ('PRIVACY_ENHANCED', 'Privacy-Enhanced'), ('FAIR_BIAS_MANAGED', 'Fair with Harmful Bias Managed')], max_length=40)),
                ('score', models.FloatField(help_text='0-1 scale or qualitative score')),
                ('notes', models.TextField(blank=True)),
                ('evaluated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('ai_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trustworthiness_evaluations', to='map.aisystem')),
                ('evaluated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
