"""Itential Integration filters."""
from nautobot.apps.filters import BaseFilterSet, SearchFilter

from nautobot_ssot.integrations.itential.models import AutomationGatewayModel, AutomationGatewayAnsibleGroupModel


class AutomationGatewayModelFilterSet(BaseFilterSet):
    """API filter for filtering automation gateway model objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "enabled": "icontains",
            "gateway": "icontains",
        },
    )

    class Meta:
        """Meta class definition."""

        model = AutomationGatewayModel
        fields = ["name", "enabled", "gateway"]


class AutomationGatewayAnsibleGroupModelFilterSet(BaseFilterSet):
    """API filter for filtering automation gateway ansible group model objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "variables": "icontains",
        },
    )

    class Meta:
        """Meta class definition."""

        model = AutomationGatewayAnsibleGroupModel
        fields = ["name", "variables"]
