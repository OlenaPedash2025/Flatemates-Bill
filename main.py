import logging
import os
from dataclasses import dataclass

from Bill import Bill
from BillSplitter import BillSplitter
from Flatmate import Flatmate
from PDFReport import FileSharer, PDFReport


# Config
@dataclass
class Config:
    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILES_DIR = os.path.join(PROJECT_DIR, "files")
    PDF_FILENAME = "flatmates_bill.pdf"
    PDF_PATH = os.path.join(FILES_DIR, PDF_FILENAME)
    IMAGE_PATH = os.path.join(FILES_DIR, "house.png")
    FILESTACK_API_KEY = "AoC797MZyTnGv5HBP6Y86z"

    @classmethod
    def ensure_files_dir_exists(cls):
        """Creates the 'files' directory if it doesn't exist."""
        os.makedirs(cls.FILES_DIR, exist_ok=True)


# Setup logging
log_file = os.path.join(Config.FILES_DIR, "app.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        Config.ensure_files_dir_exists()

        logger.info("Application started")
        print("--- Flatmates Bill Splitter ---")

        amount = float(input("Enter the bill amount (e.g. 1200): "))
        period = input("Enter the bill period (e.g. September 2026): ")

        num_flatmates = int(input("How many flatmates? "))
        flatmates = []

        for i in range(num_flatmates):
            name = input(f"\nEnter name of flatmate {i + 1}: ")
            days = int(input(f"How many days did {name} stay in the house? "))
            flatmates.append(Flatmate(name=name, days_in_house=days))

        bill_sept = Bill(amount=amount, period=period)
        splitter = BillSplitter(bill_sept, flatmates)

        report = PDFReport(
            filename=Config.PDF_PATH, splitter=splitter, image_path=Config.IMAGE_PATH
        )
        report.generate()

        file_sharer = FileSharer(
            filepath=Config.PDF_PATH, api_key=Config.FILESTACK_API_KEY
        )
        shareable_link = file_sharer.share()

        logger.info(f"Bill generated for period: {period}")
        print(
            f"\n✅ Bill generated and shared successfully! Access it here: {shareable_link}"
        )

    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        print("\nError: Please enter valid numbers for amount, days, and count.")
    except Exception as e:
        logger.error(f"Unexpected system error: {e}", exc_info=True)
        print(f"\nUnexpected system error: {e}")
