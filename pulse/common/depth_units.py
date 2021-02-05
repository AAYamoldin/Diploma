from enum import Enum
from typing import Callable


class DepthUnits(Enum):
    M = ('m', lambda x: x)  # meters
    FT = ('ft', lambda x: x * 0.3048)  # feet

    def __init__(self, alias: str, si_format: Callable) -> None:
        self.alias = alias
        self.si_format = si_format


pass
