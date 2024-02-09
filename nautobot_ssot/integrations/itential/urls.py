"""Itential Integration urls."""
from nautobot.apps.urls import NautobotUIViewSetRouter

from nautobot_ssot.integrations.itential import views

app_name = "itential"
router = NautobotUIViewSetRouter()
# ExampleModel is registered using the ViewSet
router.register("itential/automation-gateway", views.AutomationGatewayModelUIViewSet)
router.register("itential/automation-gateway-ansible-groups", views.AutomationGatewayAnsibleGroupModelUIViewSet)

urlpatterns = router.urls
