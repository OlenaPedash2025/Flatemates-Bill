# --- INFRASTRUCTURE (PDF) ---
import os

# import webbrowser
from filestack import Client
from fpdf import FPDF

from BillSplitter import BillSplitter


class PDFReport:

    def __init__(self, filename: str, splitter: BillSplitter, image_path: str):
        self.filename = filename
        self.splitter = splitter
        self.image_path = image_path

    def generate(self) -> None:
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add an icon or image (optional)
        pdf.image(self.image_path, w=30, h=30)

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
        pdf.cell(w=300, h=30, txt="TOTAL BILL", border=1, align="R")
        pdf.cell(w=150, h=30, txt=f"${self.splitter.bill.amount:.2f}", border=1, ln=1)

        # Save the file
        os.chdir("files")  # Ensure we're in the correct directory
        pdf.output(self.filename)
        # webbrowser.open(
        #     "file://" + os.path.abspath(self.filename)
        # )  # Open the PDF after generation


class FileSharer:
    def __init__(self, filepath: str, api_key: str = "AoC797MZyTnGv5HBP6Y86z"):
        self.filepath = filepath
        self.client = Client(api_key)

    def share(self):
        new_filelink = self.client.upload(filepath=self.filepath)
        return new_filelink.url
