"""
URL configuration for nistaiapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from govern.views import PolicyViewSet, RoleViewSet, RiskAppetiteViewSet
from map.views import AISystemViewSet, ContextViewSet, RiskIdentificationViewSet
from measure.views import MetricViewSet, AssessmentViewSet, MetricMeasurementViewSet
from management.views import RiskResponseViewSet, IncidentViewSet, ImprovementActionViewSet
from .views import main_dashboard

router = routers.DefaultRouter()
# Govern
router.register(r'policies', PolicyViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'risk-appetites', RiskAppetiteViewSet)
# Map
router.register(r'ai-systems', AISystemViewSet)
router.register(r'contexts', ContextViewSet)
router.register(r'risks', RiskIdentificationViewSet)
# Measure
router.register(r'metrics', MetricViewSet)
router.register(r'assessments', AssessmentViewSet)
router.register(r'measurements', MetricMeasurementViewSet)
# Management
router.register(r'risk-responses', RiskResponseViewSet)
router.register(r'incidents', IncidentViewSet)
router.register(r'improvements', ImprovementActionViewSet)

urlpatterns = [
    path('', main_dashboard, name='main-dashboard'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
