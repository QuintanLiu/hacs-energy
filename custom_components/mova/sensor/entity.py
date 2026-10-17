"""Sensor entity for mova."""

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from custom_components.mova.entity import MovaEntity
from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.helpers.typing import StateType


@dataclass(frozen=True, kw_only=True)
class MovaSensorEntityDescription(SensorEntityDescription):
    """Describes a sensor and how to read it from coordinator data."""

    value_fn: Callable[[dict[str, Any]], StateType]


class MovaSensor(SensorEntity, MovaEntity):
    """Sensor backed by one value in the coordinator payload."""

    entity_description: MovaSensorEntityDescription

    @property
    def native_value(self) -> StateType:
        """Return the value read from coordinator data."""
        return self.entity_description.value_fn(self.coordinator.data)
