import re
import unittest

from src.file_reader import read_file_lines
from src.worker import Worker


class Test(unittest.TestCase):
    test_worker = None
    file_route = "./resources/example.txt"

    @classmethod
    def setUpClass(cls) -> None:
        cls.testWorker = Worker("EXAMPLE", "")

    def test_data_file(self):
        file_lines = read_file_lines(self.file_route)
        for line in file_lines:
            matched = re.fullmatch(r"\w+=([A-Z]{2}\d{2}:\d{2}-\d{2}:\d{2},?)+\n", line)
            self.assertIsNotNone(matched, "Data file does not meet the requirements")

    def test_daily_salary_calculation_week(self):
        # Validate that minutes affect payment
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(0, 0, 3, 30, "MO"),
            "%.2f" % 87.5,
        )
        # Validate all ranges are working fine
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(0, 0, 9, 0, "MO"),
            "%.2f" % 225,
        )
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(9, 1, 18, 0, "MO"),
            "%.2f" % 134.75,
        )
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(18, 1, 0, 0, "MO"),
            "%.2f" % 119.666,
        )
        # Validate payment is calculated correctly if hours exceed the first range
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(0, 0, 11, 0, "MO"),
            "%.2f" % (225 + 30),
        )
        # Validate payment is calculated correctly if hours exceed the first and second range
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(0, 0, 19, 0, "MO"),
            "%.2f" % (225 + 135 + 20),
        )

    def test_daily_salary_calculation_weekends(self):
        # Validate that minutes affect payment
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(0, 0, 3, 30, "SA"),
            "%.2f" % 105,
        )
        # Validate all ranges are working fine
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(0, 0, 9, 0, "SA"),
            "%.2f" % 270,
        )
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(9, 1, 18, 0, "SA"),
            "%.2f" % 179.666,
        )
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(18, 1, 0, 0, "SA"),
            "%.2f" % 149.583,
        )
        # Validate payment is calculated correctly if hours exceed the first range
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(0, 0, 11, 0, "SA"),
            "%.2f" % (270 + 40),
        )
        # Validate payment is calculated correctly if hours exceed the first and second range
        self.assertEqual(
            "%.2f" % self.testWorker.calculate_daily_salary(0, 0, 19, 0, "SU"),
            "%.2f" % (270 + 180 + 25),
        )
