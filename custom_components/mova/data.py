"""
Runtime data types for mova.

Access pattern: entry.runtime_data.client / entry.runtime_data.coordinator
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import MovaApiClient
    from .coordinator import MovaDataUpdateCoordinator


type MovaConfigEntry = ConfigEntry[MovaData]


@dataclass
class MovaData:
    """Runtime data stored on the config entry after a successful setup."""

    client: MovaApiClient
    coordinator: MovaDataUpdateCoordinator
    integration: Integration
