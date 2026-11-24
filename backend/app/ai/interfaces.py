"""Provider boundary: proposals are untrusted until validated."""
from typing import Protocol

class IntentProvider(Protocol):
    def propose(self, text: str) -> dict: ...
