# --- MODELS ---
from dataclasses import dataclass

from ValidationError import ValidationError


@dataclass
class Flatmate:
    name: str
    days_in_house: int

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValidationError("Flatmate name cannot be empty.")
        if self.days_in_house < 0:
            raise ValidationError(f"{self.name} cannot have negative days.")
        if self.days_in_house > 365:
            raise ValidationError(f"{self.name} cannot stay more than 365 days.")
