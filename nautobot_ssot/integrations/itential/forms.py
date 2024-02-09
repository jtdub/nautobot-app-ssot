"""Itential Integration forms."""
from django import forms

from nautobot.apps.forms import BootstrapMixin, NautobotModelForm

from nautobot_ssot.integrations.itential.models import AutomationGatewayModel, AutomationGatewayAnsibleGroupModel


class AutomationGatewayModelForm(NautobotModelForm):
    """Generic create/update form for 'AutomationGatewayModel' objects."""

    class Meta:
        """Meta class definition."""

        model = AutomationGatewayModel
        fields = ["name", "enabled", "gateway"]


class AutomationGatewayModelFilterForm(BootstrapMixin, forms.Form):
    """Filtering/search form for `AutomationGatewayModel` objects."""

    model = AutomationGatewayModel
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(max_length=255, required=False)
    enabled = forms.BooleanField(required=False)


class AutomationGatewayAnsibleGroupModelForm(NautobotModelForm):
    """Generic create/update form for 'AutomationGatewayAnsibleGroupModel' objects."""

    class Meta:
        """Meta class definition."""

        model = AutomationGatewayAnsibleGroupModel
        fields = ["name", "variables"]


class AutomationGatewayAnsibleGroupModelFilterForm(BootstrapMixin, forms.Form):
    """Filtering/search form for `AutomationGatewayAnsibleGroupModel` objects."""

    model = AutomationGatewayAnsibleGroupModel
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(max_length=255, required=False)
    variables = forms.JSONField(required=False)
