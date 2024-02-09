"""Itential Integration Models."""
from typing import Any
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.serializers.json import DjangoJSONEncoder

from nautobot.apps.models import PrimaryModel
from nautobot.dcim.models import Location
from nautobot.extras.models import ExternalIntegration


class AutomationGatewayModel(PrimaryModel):
    """Itential Automation Gateway Model."""

    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(
        unique=True,
        max_length=255,
        blank=False,
        verbose_name="server name",
        help_text="automation gateway server name",
    )
    enabled = models.BooleanField(
        default=False,
        verbose_name="Enable or disable server SSoT sync",
        help_text="Enable or disable an automation gateway in SSoT app.",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        unique=False,
        verbose_name="Location Object",
        help_text="Location for automation gateway server to sync.",
    )
    location_descendant = models.BooleanField(
        default=True,
        verbose_name="Include descendant locations",
        help_text="Include devices from descendant locations.",
    )
    gateway = models.ForeignKey(
        ExternalIntegration,
        on_delete=models.CASCADE,
        unique=True,
        verbose_name="Automation Gateway Object",
        help_text="Automation gateway server as defined by external integration.",
    )

    def __str__(self) -> str:
        """Obtain string representation."""
        return self.name

    def save(self, *args, **kwargs: Any) -> None:
        """Format slug field."""
        self.slug = slugify(str(self))
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> Any:
        """Obtain absolute request URL."""
        return reverse("plugins:nautobot_ssot:itential:automationgatewaymodel", args=[self.slug])

    class Meta:
        """Meta class definition."""

        ordering = ["name", "enabled"]
        verbose_name = "Itential Automation Gateway Management"
        verbose_name_plural = "Itential Automation Gateway Management"


class AutomationGatewayAnsibleGroupModel(PrimaryModel):
    """Itential Automation Gateway Ansible Inventory Group Model."""

    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(
        unique=True,
        max_length=255,
        blank=False,
        verbose_name="Inventory group name",
        help_text="Itential Automation Gateway - Ansible inventory group name.",
    )
    variables = models.JSONField(
        encoder=DjangoJSONEncoder,
        blank=True,
        default=dict,
        verbose_name="Inventory group attributes",
        help_text="Ansible inventory group attributes.",
    )

    def __str__(self) -> str:
        """Obtain string representation."""
        return self.name

    def save(self, *args, **kwargs: Any) -> None:
        """Format slug field."""
        self.slug = slugify(str(self))
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> Any:
        """Obtain absolute request URL."""
        return reverse("plugins:nautobot_ssot:itential:automationgatewayansiblegroupmodel", args=[self.slug])

    class Meta:
        """Meta class definition."""

        ordering = ["name"]
        verbose_name = "Itential Automation Gateway - Ansible group inventory management."
        verbose_name_plural = "Itential Automation Gateway - Ansible group inventory management."
