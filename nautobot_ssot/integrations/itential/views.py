"""Itential Integration views."""
from nautobot_ssot.integrations.itential import filters, forms, models, tables

from nautobot.apps import views


class AutomationGatewayModelUIViewSet(views.NautobotUIViewSet):
    """Views for 'AutomationGatewayModel' objects."""

    filterset_class = filters.AutomationGatewayModelFilterSet
    filterset_form_class = forms.AutomationGatewayModelFilterForm
    form_class = forms.AutomationGatewayModelForm
    queryset = models.AutomationGatewayModel.objects.all()
    # serializer_class =
    table_class = tables.AutomationGatewayModelTable


class AutomationGatewayAnsibleGroupModelUIViewSet(views.NautobotUIViewSet):
    """Views for 'AutomationGatewayAnsibleGroupModel' objects."""

    filterset_class = filters.AutomationGatewayAnsibleGroupModelFilterSet
    filterset_form_class = forms.AutomationGatewayAnsibleGroupModelFilterForm
    form_class = forms.AutomationGatewayAnsibleGroupModelForm
    queryset = models.AutomationGatewayAnsibleGroupModel.objects.all()
    # serializer_class =
    table_class = tables.AutomationGatewayAnsibleGroupModelTable
