"""Initial contracts; no inference or execution."""
from dataclasses import dataclass, field
from enum import Enum

class Compatibility(str, Enum):
    NATIVE = "NATIVE"
    LIBRARY_REQUIRED = "LIBRARY_REQUIRED"
    FRAMEWORK_REQUIRED = "FRAMEWORK_REQUIRED"
    RUNTIME_API_REQUIRED = "RUNTIME_API_REQUIRED"
    EXTERNAL_API_REQUIRED = "EXTERNAL_API_REQUIRED"
    INDIRECT = "INDIRECT"
    UNSUPPORTED = "UNSUPPORTED"
    UNKNOWN = "UNKNOWN"

@dataclass(frozen=True)
class Intent:
    operation_id: str
    domain: str
    keywords: tuple[str, ...] = ()
    parameters: dict[str, object] = field(default_factory=dict)
    ambiguities: tuple[str, ...] = ()
