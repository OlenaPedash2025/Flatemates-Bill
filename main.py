import os

from Bill import Bill
from BillSplitter import BillSplitter
from Flatmate import Flatmate
from PDFReport import FileSharer, PDFReport

if __name__ == "__main__":
    try:
        print("--- Flatmates Bill Splitter ---")

        amount = float(input("Enter the bill amount (e.g. 1200): "))
        period = input("Enter the bill period (e.g. September 2026): ")

        name1 = input("\nEnter name of the first flatmate: ")
        days1 = int(input(f"How many days did {name1} stay in the house? "))

        name2 = input("Enter name of the second flatmate: ")
        days2 = int(input(f"How many days did {name2} stay in the house? "))

        bill_sept = Bill(amount=amount, period=period)
        flatmate1 = Flatmate(name=name1, days_in_house=days1)
        flatmate2 = Flatmate(name=name2, days_in_house=days2)

        splitter = BillSplitter(bill_sept, [flatmate1, flatmate2])

        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "files", "house.png")

        report = PDFReport(
            filename="flatmates_bill.pdf", splitter=splitter, image_path=image_path
        )
        report.generate()

        file_sharer = FileSharer(
            filepath=os.path.join(current_dir, "files", "flatmates_bill.pdf")
        )
        shareable_link = file_sharer.share()
        print(
            f"\n✅ Bill generated and shared successfully! Access it here: {shareable_link}"
        )

    except ValueError:
        print("Error: Please enter valid numbers for amount and days.")
    except Exception as e:
        print(f"Unexpected system error: {e}")
