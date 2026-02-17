# --- MODELS ---
from dataclasses import dataclass

from ValidationError import ValidationError


@dataclass
class Flatmate:
    name: str
    days_in_house: int

    def __post_init__(self):
        if self.days_in_house < 0:
            raise ValidationError(f"{self.name} cannot have negative days.")
