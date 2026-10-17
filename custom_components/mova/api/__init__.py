"""
API package for mova.

Exception hierarchy:
    MovaApiClientError (base)
    ├── MovaApiClientCommunicationError (network/timeout)
    └── MovaApiClientAuthenticationError (401/403)

The coordinator maps them onto ConfigEntryAuthFailed and UpdateFailed; nothing else
in the integration imports this package.
"""

from .client import (
    FAN_SPEEDS,
    MovaApiClient,
    MovaApiClientAuthenticationError,
    MovaApiClientCommunicationError,
    MovaApiClientError,
)

__all__ = [
    "FAN_SPEEDS",
    "MovaApiClient",
    "MovaApiClientAuthenticationError",
    "MovaApiClientCommunicationError",
    "MovaApiClientError",
]
