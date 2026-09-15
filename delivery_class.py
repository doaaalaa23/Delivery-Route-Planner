from dataclasses import dataclass

@dataclass
class Delivery:
    ID: int
    area: str
    priority: int
    weight: float
    