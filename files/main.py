# class Bill:
#     def __init__(self, amount, period):
#         self.amount = amount
#         self.period = period

#     def __str__(self):
#         return f"Bill of ${self.amount} for {self.period}"


# class FlateMater:
#     def __init__(self, name, days_in_house):
#         self.name = name
#         self.days_in_house = days_in_house

#     def __str__(self):
#         return f"FlateMater: {self.name} stayed {self.days_in_house} days"


# class BillSplitter:
#     def __init__(self, bill, flatmates):
#         self.bill = bill
#         self.flatmates = flatmates

#     def split_bill(self):
#         total_days = sum(flatmate.days_in_house for flatmate in self.flatmates)
#         if total_days == 0:
#             return {flatmate.name: 0 for flatmate in self.flatmates}

#         split_amounts = {}
#         for flatmate in self.flatmates:
#             split_amounts[flatmate.name] = (
#                 flatmate.days_in_house / total_days
#             ) * self.bill.amount
#         return split_amounts


# class PDFReport:
#     def __init__(self, file_name, bill_splitter):
#         self.file_name = file_name
#         self.bill_splitter = bill_splitter

#     def generate_report(self):
#         split_amounts = self.bill_splitter.split_bill()
#         report = "Bill Split Report\n"
#         report += f"Total Bill: ${self.bill_splitter.bill.amount}\n"
#         report += "Flatmates:\n"
#         for name, amount in split_amounts.items():
#             report += f"{name}: ${amount:.2f}\n"
#         return report

#     def save_pdf_report(self) -> None:
#         report = self.generate_report()
#         with open(self.file_name, "w") as file:
#             file.write(report)


# if __name__ == "__main__":
#     bill = Bill(1200, "September")
#     flatmate1 = FlateMater("Alice", 20)
#     flatmate2 = FlateMater("Bob", 10)

#     bill_splitter = BillSplitter(bill, [flatmate1, flatmate2])
#     pdf_report = PDFReport("bill_report.txt", bill_splitter)
#     pdf_report.save_pdf_report()
#     print("Report generated and saved as bill_report.txt")

# REFACTORING (GEMINI-4.0) - Added error handling, validation, and improved structure:

import os
from dataclasses import dataclass
from typing import Dict, List

from fpdf import FPDF


# --- CUSTOM EXCEPTIONS ---
class ValidationError(Exception):
    """Custom exception for data validation errors."""

    pass


# --- MODELS ---
@dataclass(frozen=True)
class Bill:
    amount: float
    period: str

    def __post_init__(self):
        # Validation inside a dataclass
        if self.amount <= 0:
            raise ValidationError(f"Bill amount must be positive. Got: {self.amount}")


@dataclass
class Flatmate:
    name: str
    days_in_house: int

    def __post_init__(self):
        if self.days_in_house < 0:
            raise ValidationError(f"{self.name} cannot have negative days.")


# --- BUSINESS LOGIC ---
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


# --- INFRASTRUCTURE (PDF) ---
class PDFReport:
    """Generates a professional PDF file."""

    def __init__(self, filename: str, splitter: BillSplitter):
        self.filename = filename
        self.splitter = splitter

    def generate(self) -> None:
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add an icon or image (optional)
        # pdf.image("house.png", w=30, h=30)

        # Title
        pdf.set_font(family="Arial", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Bill Info
        pdf.set_font(family="Arial", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.set_font(family="Arial", size=14, style="")
        pdf.cell(w=150, h=40, txt=self.splitter.bill.period, border=0, ln=1)

        # Table Header
        pdf.set_font(family="Arial", size=12, style="B")
        pdf.cell(w=150, h=30, txt="Name", border=1)
        pdf.cell(w=150, h=30, txt="Days stayed", border=1)
        pdf.cell(w=150, h=30, txt="Amount to Pay", border=1, ln=1)

        # Data Rows
        pdf.set_font(family="Arial", size=12)
        splits = self.splitter.calculate_split()

        for fm in self.splitter.flatmates:
            pdf.cell(w=150, h=30, txt=fm.name, border=1)
            pdf.cell(w=150, h=30, txt=str(fm.days_in_house), border=1)
            pdf.cell(w=150, h=30, txt=f"${splits[fm.name]:.2f}", border=1, ln=1)

        # Total
        pdf.set_font(family="Arial", size=12, style="B")
        pdf.cell(w=300, h=30, "TOTAL BILL", border=1, align="R")
        pdf.cell(w=150, h=30, txt=f"${self.splitter.bill.amount:.2f}", border=1, ln=1)

        # Save the file
        pdf.output(self.filename)


# --- MAIN EXECUTION WITH ERROR HANDLING ---
if __name__ == "__main__":
    try:
        # 1. Input and Validation (Business Rules)
        bill_sept = Bill(amount=1200, period="September 2026")

        people = [
            Flatmate(name="Alice", days_in_house=20),
            Flatmate(name="Bob", days_in_house=10),
        ]

        # 2. Logic execution
        splitter = BillSplitter(bill_sept, people)

        # 3. Output generation
        report = PDFReport(filename="flatmates_bill.pdf", splitter=splitter)
        report.generate()

        print(f"✅ Success! Report saved as {os.path.abspath('flatmates_bill.pdf')}")

    except ValidationError as e:
        print(f"❌ Input Error: {e}")
    except Exception as e:
        print(f"🚨 Unexpected system error: {e}")
