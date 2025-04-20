from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Policy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    version = models.CharField(max_length=50)
    effective_date = models.DateField(default=timezone.now)
    last_reviewed = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[
        ('DRAFT', 'Draft'),
        ('REVIEW', 'Under Review'),
        ('ACTIVE', 'Active'),
        ('RETIRED', 'Retired')
    ])
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    applicability = models.TextField(help_text="Scope and applicability of the policy")
    third_party_requirements = models.TextField(help_text="Requirements for third-party components and services")
    review_process = models.TextField(help_text="Policy review and update process")
    exceptions_process = models.TextField(help_text="Process for handling policy exceptions")
    compliance_requirements = models.TextField(help_text="Compliance and reporting requirements")
    lifecycle_integration = models.TextField(help_text="Integration with AI lifecycle stages")
    trustworthiness_requirements = models.TextField(help_text="Trustworthiness requirements addressed by the policy")

    class Meta:
        verbose_name_plural = "Policies"

    def __str__(self):
        return f"{self.title} - v{self.version}"

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    responsibilities = models.TextField()
    users = models.ManyToManyField(User, related_name='ai_rmf_roles')
    policies = models.ManyToManyField(Policy, related_name='assigned_roles')
    oversight_areas = models.TextField(help_text="Areas of oversight responsibility")
    third_party_oversight = models.TextField(help_text="Third-party oversight responsibilities")
    escalation_path = models.TextField(help_text="Risk and issue escalation path")
    required_qualifications = models.TextField(help_text="Required qualifications and expertise")
    delegation_authority = models.TextField(help_text="Authority delegation rules")
    lifecycle_stages = models.TextField(help_text="Lifecycle stages this role oversees.")
    trustworthiness_focus = models.TextField(help_text="Which trustworthiness characteristics this role is responsible for.")
    
    def __str__(self):
        return self.name

class RiskAppetite(models.Model):
    level = models.CharField(max_length=50, choices=[
        ('LOW', 'Low Risk'),
        ('MEDIUM', 'Medium Risk'),
        ('HIGH', 'High Risk')
    ])
    description = models.TextField()
    criteria = models.TextField()
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    approved_date = models.DateField()
    review_frequency = models.IntegerField(help_text="Review frequency in months")
    third_party_considerations = models.TextField(help_text="Risk appetite considerations for third-party components")
    review_triggers = models.TextField(help_text="Events triggering risk appetite review")
    sector_specific_factors = models.TextField(help_text="Sector-specific risk considerations")
    mitigation_requirements = models.TextField(help_text="Required risk mitigation measures")
    
    def __str__(self):
        return f"Risk Appetite - {self.level}"

class GovernanceStructure(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    structure_type = models.CharField(max_length=50, choices=[
        ('COMMITTEE', 'Governance Committee'),
        ('BOARD', 'Review Board'),
        ('WORKING_GROUP', 'Working Group'),
        ('TEAM', 'Dedicated Team')
    ])
    authority_level = models.CharField(max_length=50, choices=[
        ('ADVISORY', 'Advisory'),
        ('APPROVAL', 'Approval Authority'),
        ('OVERSIGHT', 'Oversight'),
        ('EXECUTION', 'Execution')
    ])
    members = models.ManyToManyField(User, related_name='governance_memberships')
    policies = models.ManyToManyField(Policy, related_name='governing_structures')
    parent_structure = models.ForeignKey('self', null=True, blank=True, 
                                       on_delete=models.SET_NULL, 
                                       related_name='sub_structures')
    meeting_frequency = models.CharField(max_length=50)
    charter = models.TextField(help_text="Structure's charter and operating procedures")
    responsibilities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.structure_type}"

class ThirdPartyOversight(models.Model):
    name = models.CharField(max_length=200)
    third_party_type = models.CharField(max_length=50, choices=[
        ('SOFTWARE', 'Software Provider'),
        ('HARDWARE', 'Hardware Provider'),
        ('DATA', 'Data Provider'),
        ('SERVICE', 'Service Provider'),
        ('CONSULTANT', 'Consultant')
    ])
    risk_level = models.CharField(max_length=50, choices=[
        ('LOW', 'Low Risk'),
        ('MEDIUM', 'Medium Risk'),
        ('HIGH', 'High Risk'),
        ('CRITICAL', 'Critical Risk')
    ])
    oversight_structure = models.ForeignKey(GovernanceStructure, 
                                          on_delete=models.PROTECT,
                                          related_name='overseen_parties')
    assessment_frequency = models.CharField(max_length=50)
    compliance_requirements = models.TextField()
    monitoring_approach = models.TextField()
    incident_protocol = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.third_party_type}"

class GovernanceRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ai_systems = models.ManyToManyField('map.AISystem', related_name='governance_roles')
    responsibilities = models.TextField()
    lifecycle_stages = models.TextField(help_text="Lifecycle stages this role oversees.")
    trustworthiness_focus = models.TextField(help_text="Which trustworthiness characteristics this role is responsible for.")
    
    def __str__(self):
        return self.name

class HumanAIOversight(models.Model):
    ai_system = models.ForeignKey('map.AISystem', on_delete=models.CASCADE, related_name='oversight_records')
    role = models.ForeignKey(GovernanceRole, on_delete=models.CASCADE)
    description = models.TextField()
    intervention_points = models.TextField()
    oversight_mechanisms = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Oversight for {self.ai_system.name} by {self.role.name}"

class ThirdPartyRisk(models.Model):
    ai_system = models.ForeignKey('map.AISystem', on_delete=models.CASCADE, related_name='third_party_risks')
    third_party_name = models.CharField(max_length=200)
    component_type = models.CharField(max_length=50, choices=[
        ('SOFTWARE', 'Software'),
        ('HARDWARE', 'Hardware'),
        ('DATA', 'Data'),
        ('SERVICE', 'Service'),
        ('MODEL', 'Pre-trained Model'),
    ])
    risk_description = models.TextField()
    mitigation_measures = models.TextField()
    monitoring_plan = models.TextField()
    last_reviewed = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.third_party_name} risk for {self.ai_system.name}"
