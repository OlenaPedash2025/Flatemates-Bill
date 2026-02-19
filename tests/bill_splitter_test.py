import unittest

from Bill import Bill
from BillSplitter import BillSplitter
from Flatmate import Flatmate
from ValidationError import ValidationError


class TestBillSplitter(unittest.TestCase):

    def setUp(self):

        self.bill = Bill(amount=1200, period="September 2026")

        self.flatmate1 = Flatmate(name="Alice", days_in_house=20)

        self.flatmate2 = Flatmate(name="Bob", days_in_house=10)

    def test_calculate_split(self):

        splitter = BillSplitter(self.bill, [self.flatmate1, self.flatmate2])

        split = splitter.calculate_split()

        self.assertAlmostEqual(split["Alice"], 800.0)

        self.assertAlmostEqual(split["Bob"], 400.0)

    def test_empty_flatmates_raises_error(self):

        with self.assertRaises(ValidationError):

            BillSplitter(self.bill, [])

    def test_zero_days_returns_zero(self):

        flatmate = Flatmate(name="Charlie", days_in_house=0)

        splitter = BillSplitter(self.bill, [flatmate])

        split = splitter.calculate_split()

        self.assertEqual(split["Charlie"], 0.0)


if __name__ == "__main__":

    unittest.main()
