"""Itential Integration table definitions."""
import django_tables2 as tables

from nautobot.apps.tables import (
    BaseTable,
    ButtonsColumn,
    ToggleColumn,
)

from nautobot_ssot.integrations.itential.models import AutomationGatewayModel, AutomationGatewayAnsibleGroupModel


class AutomationGatewayModelTable(BaseTable):
    """Table for the list view of the 'AutomationGatewayModel' objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = ButtonsColumn(AutomationGatewayModel)

    class Meta:
        """Meta definition."""

        model = AutomationGatewayModel
        fields = ["pk", "name"]


class AutomationGatewayAnsibleGroupModelTable(BaseTable):
    """Table for the list view of the 'AutomationGatewayAnsibleGroupModel' objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = ButtonsColumn(AutomationGatewayAnsibleGroupModel)

    class Meta:
        """Meta definition."""

        model = AutomationGatewayAnsibleGroupModel
        fields = ["pk", "name"]
