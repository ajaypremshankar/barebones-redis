from dataclasses import dataclass


@dataclass
class FiredCommand:
    command: str
    params: [str] = None