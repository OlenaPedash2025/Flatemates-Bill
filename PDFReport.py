import os

from filestack import Client
from fpdf import FPDF


class PDFReport:
    def __init__(self, filename: str, splitter, image_path: str):
        self.filename = filename
        self.splitter = splitter
        self.image_path = image_path

    def generate(self):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        if os.path.exists(self.image_path):
            pdf.image(self.image_path, w=30, h=30)

        # Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=self.splitter.bill.period, border=0, ln=1)

        # Flatmates data
        pdf.set_font(family="Times", size=12)
        for flatmate in self.splitter.flatmates:
            name_text = f"{flatmate.name}:"
            amount_text = str(round(self.splitter.calculate_share(flatmate), 2))

            pdf.cell(w=100, h=25, txt=name_text, border=0)
            pdf.cell(w=150, h=25, txt=amount_text, border=0, ln=1)

        pdf.output(self.filename)


class FileSharer:

    def __init__(self, filepath, api_key=""):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
