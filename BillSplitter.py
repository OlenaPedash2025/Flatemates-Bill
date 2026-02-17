# --- BUSINESS LOGIC ---
from typing import Dict, List

from Bill import Bill
from Flatmate import Flatmate
from ValidationError import ValidationError


class BillSplitter:
    def __init__(self, bill: Bill, flatmates: List[Flatmate]):
        if not flatmates:
            raise ValidationError(
                "At least one flatmate is required to split the bill."
            )
        self.bill = bill
        self.flatmates = flatmates

    @property
    def total_days(self) -> int:
        return sum(fm.days_in_house for fm in self.flatmates)

    def calculate_split(self) -> Dict[str, float]:
        total = self.total_days
        if total == 0:
            return {fm.name: 0.0 for fm in self.flatmates}

        return {
            fm.name: (fm.days_in_house / total) * self.bill.amount
            for fm in self.flatmates
        }
