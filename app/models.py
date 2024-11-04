from dataclasses import dataclass

@dataclass
class ParsedArgs:
    args: dict[str, str]

@dataclass
class FiredCommand:
    command: str
    args: ParsedArgs = None