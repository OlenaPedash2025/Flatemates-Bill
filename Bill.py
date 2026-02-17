from dataclasses import dataclass

from ValidationError import ValidationError


@dataclass(frozen=True)
class Bill:
    amount: float
    period: str

    def __post_init__(self):
        # Validation inside a dataclass
        if self.amount <= 0:
            raise ValidationError(f"Bill amount must be positive. Got: {self.amount}")
